import os

from pytorch_agents.a2c import A2C
from pytorch_agents.ddpg import DDPG
from pytorch_agents.dqn import DQN
from pytorch_agents.her import HER
from pytorch_agents.ppo import PPO
from pytorch_agents.sac import SAC
from pytorch_agents.td3 import TD3

# Read version from file
version_file = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_file, "r") as file_handler:
    __version__ = file_handler.read().strip()
