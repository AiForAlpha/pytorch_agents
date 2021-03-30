# Welcome to the pytorch_agents setup.py.
# this setup file is following guidelines and recommendation from pytorch
#

from __future__ import print_function
import sys
import platform
python_min_version = (3, 6, 2)

# We do not support any python below the python_min_version
python_min_version_str = '.'.join(map(str, python_min_version))
if sys.version_info < python_min_version:
    print("You are using Python {}. Python >={} is required.".format(platform.python_version(),
                                                                     python_min_version_str))
    sys.exit(-1)

long_description = """
# Pytorch agents
 Pytorch agents is a collection of implementations of deep reinforcement learning algorithms in PyTorch. 
 Our implementations are roughly on par with the ones in published papers.
 In terms of Deep RL algorithms, it is inspired and borrows from OpenAI, stable baseline and tf_agents but only using pytorch
 In terms of interface, it is inspired from scikit learn.
 
 It aims at making the usage of deep RL easier for the research community and industry to reproduce, finetune and improve DeepRL
 In terms of interface, it aims at providing a unified interface for any deep RL agent


## Links
Repository:
https://github.com/AiForAlpha/pytorch_agents
Documentation:
https://AiForAlpha.readthedocs.io/en/master/

## Quick example
The library aims at following a simple and unified syntax for Reinforcement Learning algorithms using Gym, as this
is done for sklearn for supervised learning algorithms. It is inspired by stable baseline with a focus
on hyperparameters tuning thanks to optuna. The core idea is to create an environment that follows gym interface and 
be able to leverage Bayesian and Black box optimization for hyper parameters tuning


```python
import gym
from pytorch_agents import DDPG
env = gym.make('CartPole-v1')
model = DDPG('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=10000)
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()
```
""" 

setup(
    name="pytorch_agents",
    packages=[package for package in find_packages() if package.startswith("pytorch_agents")],
    package_data={"pytorch_agents": ["py.typed", "version.txt"]},
    install_requires=[
        "gym>=0.17",
        "joblib",
        "numpy",
        "torch>=1.4.0",
        "tqdm",
        # For saving models
        "cloudpickle",
        # For reading data and logs
        "pandas",
        # Plotting learning curves
        "matplotlib",
    ],
    extras_require={
        "tests": [
            # Run tests and coverage
            "pytest",
            "pytest-cov",
            "pytest-env",
            "pytest-xdist",
            # Type check
            "pytype",
            # Lint code
            "flake8>=3.8",
            # Find likely bugs
            "flake8-bugbear",
            # Sort imports
            "isort>=5.0",
            # Reformat
            "black",
        ],
        "docs": [
            "sphinx",
            "sphinx-autobuild",
            "sphinx-rtd-theme",
            # For spelling
            "sphinxcontrib.spelling",
            # Type hints support
            "sphinx-autodoc-typehints",
        ],
        "extra": [
            # For render
            "opencv-python",
            # For atari games,
            "atari_py~=0.2.0",
            "pillow",
            # Tensorboard support
            "tensorboard>=2.2.0",
            # Checking memory taken by replay buffer
            "psutil",
        ],
    },
    description="Pytorch version of OpenAI Baseline, implementations of deep reinforcement learning algorithms.",
    author="David Saltiel, Eric Benhamou",
    url="https://https://github.com/AiForAlpha/pytorch_agents",
    author_email="david.saltiel@aiforalpha.com",
    keywords="deep-reinforcement-learning-algorithms reinforcement-learning machine-learning "
    "gym openai stable baselines toolbox python data-science",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
)

