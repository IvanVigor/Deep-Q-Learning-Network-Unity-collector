# Project Report

The report provides an overview of the main concepts faced during this project. 

## Reinforcement Learning Framework

In this reinforcement learning scenario, the agent's goal is to maximize the expected cumulative reward. The reward can be accumulated by collecting yellow bananas. The state is expressed through a tuple of `37` values. The Agent can provide `4` different actions. 

The agent is in charge of choosing the best action for every position. The Q-table aims to define for each state, the reward associated with each action. This Q-Table can be visualized as a matrix, which a reward is assigned to each action for every possible state. 

This matrix can be easily associated with a discrete space, where the values do not continue. In this latter, the best solution that can be adopted is an approximation of the best action to select. In order to face this problem for our banana environment, we used the Deep Q-Learning approach.

## Deep Q-Learning

This method is based on the usage of a deep neural network for selecting the best action. The neural network works using the Bellman Equation of Q-Learning:

![results](https://github.com/IvanVigor/Deep-Q-Learning-Network-Unity-collector/blob/master/pictures/CodeCogsEqn.svg)

The classical model of this Deep Q-Learning Network can be seen in the picture below. As you can see, the network visualizes as input the frames of the environment and then provide a distribution over all the possible actions. For this implementation, we used a two hidden layer architecture. For each hidden layer, we used `64` hidden units with ReLU activation function. The input sample has `37` features and the output has `4` dimensions (one for each action). 

At each state, the model needs to find out the best trade-off between the exploration and exploitation policy. As we said previously, the Agent needs to maximize the final reward. On one hand, the Agent needs to increase the final reward as much as possible. On the other hand, the Agent should explore new paths for the identification of new valuable paths. This is simply done with a random selection of the action for each state with a probability expressed by a variable epsilon.

The probability to take a random action decrease progressively according to these parameters:
`eps_start=1.0, eps_end=0.01, eps_decay=0.995`

![results](https://cdn-images-1.medium.com/max/1600/1*T54Ngd-b_CKcP3N6hyXLVg.png)

The Deep Q-learning network is based on two fundamentals aspects: 

1) Replay Buffer
2) Fixed Target

Replay Memory avoids learning from a highly correlated temporal sequence of states which are not useful for reaching a valuable solution. During the training phase, a set of random samples are injected for diversification of sequence.

The learning sequence may be not stable if we learn a guess from a guess. According to that, the weights are compared with a fixed value for a sequence of steps. 

## HyperParameters
* `eps_start=1.0, eps_end=0.01, eps_decay=0.995  # Starting epsilon value, minimum value and decay` 
* `BUFFER_SIZE = int(1e5)  # replay buffer size`
* `BATCH_SIZE = 64         # minibatch size`
* `GAMMA = 0.99            # discount factor`
* `TAU = 1e-3              # for soft update of target parameters`
* `LR = 5e-4               # learning rate `
* `UPDATE_EVERY = 4        # how often to update the network (do not decrease this value)` 

##  Results

The plot below illustrates the increasing rewards associated with the Agent performance into the Unity Environment.
The average of the results (orange line) reaches a value equal of `16` at `800` epochs. 

![results](https://github.com/IvanVigor/Deep-Q-Learning-Network-Unity-collector/blob/master/pictures/performance.png)

## Future Work

Possible future activities for improving the performances:

* Replay Buffer with a similarity detection of past episodes - Local Fusion approach.

* Duelling DQN 

* CNN Agent for understanding from Pixels of the environment state. 

