from typing import List, Tuple

from commitment_agent import CommitmentAgent
from matrix_games import MatrixGame


def train_commitment(env: MatrixGame, t_max: int, n_min: int, n_init: int,
                     p: float, evaluate_every: int) -> Tuple[List[CommitmentAgent], List]:
    """
    Training loop.

    :param env: The gym environment.
    :param t_max: The number of timesteps.
    :param n_min: The threshold of number of samples to consider the average reward of a commitment sequence reliable.
    :param n_init: The number of sequences to initialize by exploring.
    :param p: The probability to start a new sequence by exploring randomly and uniformly.
    :param evaluate_every: Frequency of evaluation to get the current greedy action.
    :return: Tuple containing the list of trained agents and a list containing the greedy joint actions at each evaluation step.
    """
    agents = [CommitmentAgent(env.num_actions, t_max, n_min, n_init, p) for _ in range(env.num_agents)]
    # TODO: complete.
    raise NotImplementedError


if __name__ == '__main__':
    env = MatrixGame()
    # TODO: complete.
