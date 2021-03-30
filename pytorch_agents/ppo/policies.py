# This file is here just to define MlpPolicy/CnnPolicy
# that work for PPO
from pytorch_agents.common.policies import ActorCriticCnnPolicy, ActorCriticPolicy, register_policy

MlpPolicy = ActorCriticPolicy
CnnPolicy = ActorCriticCnnPolicy

register_policy("MlpPolicy", ActorCriticPolicy)
register_policy("CnnPolicy", ActorCriticCnnPolicy)
