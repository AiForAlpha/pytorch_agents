# pytorch_agents
Deep RL library using pytorch

# Pytorch agents
pytorch_agents is a collection of high-quality implementations of deep reinforcement learning algorithms.

## Prerequisites 
pytorch_agents requires python3 (>=3.6) with the development headers. 
You'll also need system packages CMake, OpenMPI and zlib. Those can be installed as follows
  
## Virtual environment
From the general python package sanity perspective, it is a good idea to use virtual environments (virtualenvs) to make sure packages from different projects do not interfere with each other. You can install virtualenv (which is itself a pip package) via
Virtualenvs are essentially folders that have copies of python executable and all python packages.
To create a virtualenv called pa with python3, one runs 
```bash
conda create --name pa
```
To activate a virtualenv: 
```
conda activate pa
```
More thorough tutorial on virtualenvs and options can be found [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) 

## Installation
- Clone the repo and cd into it:
    ```bash
    git clone https://https://github.com/AiForAlpha/pytorch_agents
    cd src
    ```
- Then install the required packages
    ```bash 
    
    ```

## Testing the installation
All unit tests in baselines can be run using pytest runner:
```
pip install pytest
pytest
```

## Training models

## Saving, loading and visualizing models

## Subpackages
- [A2C](pytorch_agents/a2c)
- [ACER](pytorch_agents/acer)
- [ACKTR](pytorch_agents/acktr)
- [DDPG](pytorch_agents/ddpg)
- [DQN](pytorch_agents/dqn)
- [GAIL](pytorch_agents/gail)
- [HER](pytorch_agents/her)
- [PPO](pytorch_agents/ppo) 
- [TRPO](pytorch_agents/trpo)


