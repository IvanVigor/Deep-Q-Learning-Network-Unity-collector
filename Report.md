# Project Report

The report provides an overview of the main concepts faced during this project. 

## Reinforment Learning Framework

In this reinforcement learning scenario, the agent's goal is to maximaze the expected cumulative reward. The reward can be accumulated by collecting yellow bananas. The state is expressed through a tuple of 37 values. The Agent can provide 4 different actions. 

The agent is in charge of choosing the best action for every position. The Q-table aims to define for each state, the reward associated to each action. This Q-Table can be visualized as a matrix, which a reward is assigned to each action for every possible state. 

This matrix can be easily associated to a discrete space, where the values are not continue. In this latter, the best solution that can be adopted is an approximation of the best action to select. In order to face this problem for our banana environment we used the Deep Q-Learning approach.

# Deep Q-Learning


![results](https://cdn-images-1.medium.com/max/1600/1*T54Ngd-b_CKcP3N6hyXLVg.png)


##  Results

The plot below illustrates the increasing rewards associated to the Agent performance into the Unity Environment.
![results](https://github.com/IvanVigor/Deep-Q-Learning-Network-Unity-collector/blob/master/pictures/DQN_Agent_Performances.png)
The average of the results (orange line) reaches a value equal to 15 at 1800 epochs.
