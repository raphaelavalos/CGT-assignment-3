from typing import Tuple, List

import numpy as np
from numpy import ndarray

from iql_agent import IQLAgent
from matrix_games import MatrixGame


def train_iql(env: MatrixGame, t_max: int, evaluate_every: int, num_evaluation_episodes: int,
              epsilon_max: float = None, epsilon_min: float = None,
              epsilon_decay: float = None) -> Tuple[List[IQLAgent], ndarray, ndarray, list]:
    """
    Training loop.

    :param env: The gym environment.
    :param t_max: The number of timesteps.
    :param evaluate_every: Evaluation frequency.
    :param num_evaluation_episodes: Number of episodes for evaluation.
    :param epsilon_max: The maximum epsilon of epsilon-greedy.
    :param epsilon_min: The minimum epsilon of epsilon-greedy.
    :param epsilon_decay: The decay factor of epsilon-greedy.
    :return: Tuple containing the list of agents, the returns of all training episodes, the averaged evaluation
    return of each evaluation, and the list of the greedy joint action of each evaluation.
    """
    agents = [IQLAgent(env.num_actions, epsilon_max, epsilon_min, epsilon_decay)
              for _ in range(env.num_agents)]
    # TODO: complete.
    raise NotImplementedError



if __name__ == '__main__':
    env = MatrixGame()
    # TODO: complete.
