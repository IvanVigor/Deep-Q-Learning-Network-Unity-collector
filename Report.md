# Project Report

The report provides an overview of the main concepts faced during this project. 

## Reinforcement Learning Framework

In this reinforcement learning scenario, the agent's goal is to maximize the expected cumulative reward. The reward can be accumulated by collecting yellow bananas. The state is expressed through a tuple of 37 values. The Agent can provide 4 different actions. 

The agent is in charge of choosing the best action for every position. The Q-table aims to define for each state, the reward associated with each action. This Q-Table can be visualized as a matrix, which a reward is assigned to each action for every possible state. 

This matrix can be easily associated with a discrete space, where the values do not continue. In this latter, the best solution that can be adopted is an approximation of the best action to select. In order to face this problem for our banana environment, we used the Deep Q-Learning approach.

# Deep Q-Learning

This method is based on the usage of a deep neural network for selecting the best action. The neural network works using the Bellman Equation of Q-Learning:

![results](https://github.com/IvanVigor/Deep-Q-Learning-Network-Unity-collector/blob/master/pictures/CodeCogsEqn.svg)

The classical model of this Deep Q-Learning Network can be seen in the picture below. As you can see, the network visualizes as input the frames of the environment and then provide a distribution over all the possible actions.

![results](https://cdn-images-1.medium.com/max/1600/1*T54Ngd-b_CKcP3N6hyXLVg.png)

The Deep Q-learning network is based on two fundamentals aspects:

1) Replay Memory
2) Fixed Target

Replay Memory avoids to learn from highly correlated temporal sequence of states which are not useful for reaching a valuable solution. During the training phase, a set of random samples are injected for a diversification of the sample sequence.

The learning sequence may be not stable if we learn a guess from a guess. According to that, the weights are compared with a fixed value for a sequence of steps. 

##  Results

The plot below illustrates the increasing rewards associated with the Agent performance into the Unity Environment.
![results](https://github.com/IvanVigor/Deep-Q-Learning-Network-Unity-collector/blob/master/pictures/DQN_Agent_Performances.png)
The average of the results (orange line) reaches a value equal of 15 at 1800 epochs.
