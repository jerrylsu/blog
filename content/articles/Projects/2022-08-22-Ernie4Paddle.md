date: 2022-08-22 11:17:17
author: Jerry Su
slug: Ernie4Paddle
title: Ernie4paddle
category: 
tags: Project, NLP
toc: show

Ernie4Paddle
============

Update
----
- 2024.06.05: 新增[OpenChartUCSGModel](https://www.jerrylsu.net/articles/Universal-Chart-Structural-Multimodal-Generation-and-Extraction.html)模型评估工具及Benchmark。
- 2024.05.24: 新增[OpenChartUCSGModel](https://www.jerrylsu.net/articles/Universal-Chart-Structural-Multimodal-Generation-and-Extraction.html)多模态图表结构化抽取推理引擎open_chart_uce_api。
- 2024.05.06: 新增DocTuning小样本建模平台。
- 2023.08.02: 新增UIEX模型算子预处理uiex_async_server_api服务，提供对PDF文档的支持。
- 2023.07.17: 新增JupyterLab工具以及对应Tools脚本。
- 2023.06.15: 新增UTCX通用文档分类引擎utcx_classify_api。
- 2023.06.06: 新增UTC Trainer标准训练器组件。
- 2023.04.02: 新增UTC通用文本分类引擎utc_classify_api。
- 2023.03.02: 新增UIEX Trainer标准训练器组建。
- 2023.02.20: 新增UIE Trainer标准训练器组件。
- 2023.02.10: 新增UIEX多模态文档抽取推理引擎uiex_extract_api。
- 2023.01.12: 新增多语言跨模态布局增强文档抽取引擎ernie_layoutx_extract_api。
- 2023.01.05: 迁移新增UIE实体抽取推理引擎uie_extract_api。
- 2022.12.15: 新增文本向量化推理引擎ernie_as_service_api。
- 2022.11.14: 新增页面分类定位推理引擎text_classification_api。
- 2022.10.23: 新增实体抽取推理引擎gp_extract_api。
- 2022.10.18: 新增对抗训练算子FGM（Fast Gradient Method）和对抗训练控制参数。
- 2022.10.17: 新增对抗训练算子AWP（Adversarial Weight Perturbation）。
- 2022.09.07: 新增data数据工程，支持各种版式、流式文档转换成文本格式的数据集。
- 2022.09.06: 新增VisualDL可视化组件，支持超参数，模型结构，输入文本等可视化和实验数据持久化。
- 2022.08.26: 新增基于PaddleNLP标准化训练器Trainer，支持自定义拓展。
- 2022.08.24: 新增[GlobalPointer](https://www.jerrylsu.net/articles/Global-Pointer-Multi-Head-Attention-without-Value-Operation.html)模型Metric评价指标F1和准召。
- 2022.08.24: 新增Multi Cross Entropy损失函数。
- 2022.08.23: Ernie4Paddle架构重构，功能模块化，代码解耦。
- 2022.08.22: 基于PaddleNLP继承重写Ernie [GlobalPointer](https://www.jerrylsu.net/articles/Global-Pointer-Multi-Head-Attention-without-Value-Operation.html)模型，重写ErnieEmbedding层增加层次分解编码。