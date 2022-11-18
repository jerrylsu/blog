date: 2022-11-03 11:17:17
author: Jerry Su
slug: Paddle-Adversarial-Train
title: Paddle adversarial train
category: 
tags: Paddle


```python
import paddle
```


```python
class FGM(object):
    """Fast Gradient Method.
    """
    def __init__(self, model, eps=1.):
        self.model = (model.module if hasattr(model, "module") else model)
        self.eps = eps
        self.backup = {}

    def attack(self, emb_name='embedding'):
        """only attack embedding
        """
        for name, param in self.model.named_parameters():
            if not param.stop_gradient and emb_name in name:
                self.backup[name] = param.clone()        # 备份
                norm = paddle.norm(param.grad)           # embedding梯度
                if norm and not paddle.isnan(norm):
                    r_at = self.eps * param.grad / norm  # 计算扰动
                    param.add(r_at)                      # 注入扰动

    def restore(self, emb_name='embedding'):
        """Restore model parameter to correct position; 
        FGM do not perturbe weights, it perturb gradients;
        Call after loss.backward(), before optimizer.step()
        """
        for name, param in self.model.named_parameters():
            if not param.stop_gradient and emb_name in name:
                assert name in self.backup
                param.set_value(self.backup[name])      # 删除扰动
        self.backup = {}
```


```python
class AWP(object):
    """Adversarial Weight Perturbation.
    """
    def __init__(
        self,
        model,
        optimizer=None,
        adv_param="weight",
        adv_lr=1,
        adv_eps=0.001,
        start_epoch=0,
        adv_step=1,
        scaler=None
    ):
        self.model = model
        self.optimizer = optimizer
        self.adv_param = adv_param
        self.adv_lr = adv_lr
        self.adv_eps = adv_eps
        self.adv_step = adv_step
        self.backup = {}
        self.backup_eps = {}
        self.scaler = scaler

    def perturb(self):
        """Perturb model parameters for AWP gradient
        Call before loss and loss.backward()
        """
        if (self.adv_lr == 0):
            return None

        self._save() 
        self._attack_step()

    def _attack_step(self):
        e = 1e-6
        for name, param in self.model.named_parameters():
            if (not param.stop_gradient) and (param.grad is not None) and (self.adv_param in name):
                norm1 = paddle.norm(param.grad)
                norm2 = paddle.norm(param.detach())
                if norm1 != 0 and not paddle.isnan(norm1):
                    r_at = self.adv_lr * param.grad / (norm1 + e) * (norm2 + e)
                    param.add(r_at)
                    param = paddle.min(
                        paddle.max(param, self.backup_eps[name][0]), self.backup_eps[name][1]
                    )
                # param.data.clamp_(*self.backup_eps[name])

    def _save(self):
        for name, param in self.model.named_parameters():
            if (not param.stop_gradient) and (param.grad is not None) and (self.adv_param in name):
                if name not in self.backup:
                    self.backup[name] = param.clone()
                    grad_eps = self.adv_eps * param.abs().detach()
                    self.backup_eps[name] = (
                        self.backup[name] - grad_eps,
                        self.backup[name] + grad_eps,
                    )

    def restore(self,):
        """Restore model parameter to correct position; 
        AWP do not perturbe weights, it perturb gradients;
        Call after loss.backward(), before optimizer.step()
        """
        for name, param in self.model.named_parameters():
            if name in self.backup:
                param.set_value(self.backup[name])
        self.backup = {}
        self.backup_eps = {}
```

## How to use ?


```python
model = ...
fgm = FGM(model=model) if args.do_adversarial_train else None
self.adv = fgm
```


```python
# FGM adversarial train
if self.adv and self.state.epoch > self.args.num_train_epochs // 2:
    self.adv.attack()
    # FGM
    with self.autocast_smart_context_manager():
        loss_adv = self.compute_loss(model, inputs, labels)
    if self.args.gradient_accumulation_steps > 1:
        loss_adv = loss_adv / self.args.gradient_accumulation_steps
    loss_adv.backward()
    self.adv.restore()
```
