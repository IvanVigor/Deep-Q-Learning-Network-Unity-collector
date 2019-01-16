# Deep Q-Learning Network  


This repository illustrate and provide the entire code for a Deep Q-Learning Network for creating an autonomous agent which collects bananas into the Unity env.

##  Problem Description

The Agent is in charge of collect bananas in a large, square world. In this environment, the bananas have two different colors: blue and yellow. The Agent aquires a value of +1 for each yeallow banana, and a reward of -1 for each blue banana. The main goal, as a reinforcement learning problem is to maximaze the final reward. This means that the Agent needs to collect only yellow bananas. 

![Alt Text](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/June/5b1ab4b0_banana/banana.gif)

The space is provided as a tuple of 37 dimensions. Each dimension ranges between [0,1], with features refering to agent's velocity and ray-based perception of objects around the agent's forward direction. Four discrete actions are available, corresponding to:

- **'0'** - move forward.
- **'1'** - move backward.
- **'2'** - turn left.
- **'3'** - turn right.

##  Dependencies

To set up your python environment to run the code in this repository, follow the instructions below.

1. Create (and activate) a new environment with Python 3.6.

	- __Linux__ or __Mac__: 
	```bash
	conda create --name drlnd python=3.6
	source activate drlnd
	```
	- __Windows__: 
	```bash
	conda create --name drlnd python=3.6 
	activate drlnd
	```
	
2. Follow the instructions in [this repository](https://github.com/openai/gym) to perform a minimal install of OpenAI gym.  
	- Next, install the **classic control** environment group by following the instructions [here](https://github.com/openai/gym#classic-control).
	- Then, install the **box2d** environment group by following the instructions [here](https://github.com/openai/gym#box2d).
	
3. Clone the repository (if you haven't already!), and navigate to the `python/` folder.  Then, install several dependencies.

```bash
git clone https://github.com/udacity/deep-reinforcement-learning.git
cd deep-reinforcement-learning/python
pip install .
```
4. Create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `drlnd` environment.  
```bash
python -m ipykernel install --user --name drlnd --display-name "drlnd"
```

5. Before running code in a notebook, change the kernel to match the `drlnd` environment by using the drop-down `Kernel` menu. 

##  PyTorch

The model has been developed using PyTorch library. The Pytorch library is available over the main page: https://pytorch.org/

Through the usage of Anaconda, you can download directly the pytorch and torchvision library. 

```bash
conda install pytorch torchvision -c pytorch
```

## Additional Libraries

In addition to PyTorch, in this repository has been used also Numpy. The 


## Files Description

There are 4 files: 
- model.py: Agent PyTorch neural network.
- Navigation.ipynb: Jupyter notebook which illustrates the sequence of actions for creating the Agent.
- dqn_agent.py: DQN Class and training section.
- report.pdf: A small description of the code used in this Github repository

There is a directory of pictures with the results achieved.

##  License
The code is provided with MIT license 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
## Author
Ivan Vigorito




