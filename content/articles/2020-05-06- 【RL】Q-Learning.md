Status: published
Date: 2020-05-06 06:53:33
Author: Jerry Su
Slug: 【RL】Q-Learning
Title: 【RL】Q Learning
Category: Reinforcement Learning 
Tags: Reinforcement Learning 

[TOC]

```python
import numpy as np
import gym
import random
import time
from IPython.display import clear_output
```

```python
"""Creating the Environment"""
env = gym.make("FrozenLake-v0")
```


```python
"""Creating the Q-Table and initializing all the Q-Values to zero for each state-action pair."""

action_space_size = env.action_space.n
state_space_size = env.observation_space.n
q_table = np.zeros((state_space_size, action_space_size))
q_table
```
    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])

```python
"""Initializing the parametres for Q-Learning algorithm"""
num_episodes = 10000
max_steps_per_episode = 100

learning_rate = 0.1 
discount_rate = 0.99

# for exploration-exploitation trade-off: epsilon-greedy policy
exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_decay_rate = 0.001
```

### Training


```python
rewards_all_episodes = []

# Q-Learning algorithm
for episode in range(num_episodes):
    # initialize new episode parameter
    state = env.reset()
    done = False
    rewards_current_episode = 0
    
    for step in range(max_steps_per_episode):
        
        # exploration-exploitation trade-off: agent explores or 
        # exploits the environment in this time-step.
        exploration_rate_threshold = random.uniform(0, 1)
        if exploration_rate_threshold > exploration_rate:
            action = np.argmax(q_table[state, :])
            # print("policy action: {}".format(action))
        else:
            action = env.action_space.sample()
            # print("random action: {}".format(action))
        
        # taking action
        new_state, reward, done, info = env.step(action)
        
        # Update Q-Table for Q(s, a)
        q_table[state, action] = (1 - learning_rate) * q_table[state, action] \
        + learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
        
        # transition to the next state
        state = new_state
        rewards_current_episode += reward
        
        if done is True:
            break

    # exploration rate decay
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) \
                       * np.exp(-exploration_decay_rate * episode)
    
    rewards_all_episodes.append(rewards_current_episode)

# Calculate and print the average reward per thousand episodes
rewards_per_thosand_episodes = np.split(np.array(rewards_all_episodes),num_episodes/1000)
count = 1000
for r in rewards_per_thosand_episodes:
    print(count, ": ", str(sum(r/1000)))
    count += 1000
```

    ********Average reward per thousand episodes********
    
    1000 :  0.057000000000000044
    2000 :  0.21100000000000016
    3000 :  0.3760000000000003
    4000 :  0.5990000000000004
    5000 :  0.6180000000000004
    6000 :  0.6640000000000005
    7000 :  0.6830000000000005
    8000 :  0.6610000000000005
    9000 :  0.6620000000000005
    10000 :  0.6840000000000005

```python
q_table
```

    array([[0.57489904, 0.52079771, 0.51748556, 0.48793235],
           [0.42212101, 0.26917985, 0.34271382, 0.5203443 ],
           [0.41164658, 0.4280145 , 0.40879341, 0.48422459],
           [0.32569816, 0.37293149, 0.36049325, 0.46078178],
           [0.59779375, 0.39344761, 0.32263887, 0.28641992],
           [0.        , 0.        , 0.        , 0.        ],
           [0.29567781, 0.13502175, 0.22982768, 0.21277447],
           [0.        , 0.        , 0.        , 0.        ],
           [0.35598767, 0.48995879, 0.42166608, 0.62406041],
           [0.45348018, 0.70820025, 0.49994856, 0.49117507],
           [0.58119802, 0.44345026, 0.26892586, 0.38122787],
           [0.        , 0.        , 0.        , 0.        ],
           [0.        , 0.        , 0.        , 0.        ],
           [0.33119261, 0.66936184, 0.77995132, 0.48286706],
           [0.72566318, 0.8968122 , 0.70399676, 0.7334053 ],
           [0.        , 0.        , 0.        , 0.        ]])


### Inference


```python
# The Q-Table is the konwledge we gained by training.
# agent choose the best action from each state according to the Q-Table.
for episode in range(3):
    state = env.reset()
    done = False
    print("EPISODE {}".format(episode + 1))
    time.sleep(1)
    for step in range(max_steps_per_episode):
        
        # show the current state of environment on screen.
        env.render()
        time.sleep(0.3)
        clear_output(wait=True)
        # choose action with highest Q-Value for current state.
        action = np.argmax(q_table[state, :])
        # update the state, reward, done for the action.
        new_state, reward, done, info = env.step(action)
        
        if done:
            clear_output(wait=True)
            env.render()
            if reward == 1:
                print("Reached the goal!")
                time.sleep(3)
                clear_output(wait=True)
            else:
                print("Fell the hole!")
                time.sleep(3)
                clear_output(wait=True)
            break
        state = new_state
env.close()
```

      (Down)
    SFFF
    FHFH
    FFFH
    HFF[41mG[0m
    Reached the goal!