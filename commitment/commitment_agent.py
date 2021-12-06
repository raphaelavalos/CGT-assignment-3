from typing import Tuple
from numpy import ndarray


def generate_t_to_seq(t_max: int) -> Tuple[dict, ndarray]:
    """
    Function that generates the different commitment sequences.

    Example
    --------------------------
    >>> (id_to_seq, t_to_seq) = generate_t_to_seq(10)
    >>> id_to_seq
    {0: array([0, 2, 5, 9]), 1: array([1, 4, 8]), 2: array([3, 7]), 3: array([6])}
    >>> t_to_seq
    array([0, 1, 0, 2, 1, 0, 3, 2, 1, 0])

    :param t_max: The number of timesteps.
    :return: (id_to_seq, t_to_seq) with id_to_seq a dictionary mapping
            sequences number to an array containing all its timesteps. t_to_seq is a array of size t_max with t_to_seq[t]
            being the sequence number of the timestep t.
    """
    # TODO: complete.
    raise NotImplementedError


class CommitmentAgent:
    """
    The agent class that applies commitment sequences.
    """

    def __init__(self, num_actions: int, t_max: int, n_min: int, n_init: int, p: float):
        """
        :param num_actions: The number of actions.
        :param t_max: The number of timesteps.
        :param n_min: The threshold of number of samples to consider the average reward of a commitment sequence reliable.
        :param n_init: The number of sequences to initialize by exploring.
        :param p: The probability to start a new sequence by exploring randomly and uniformly.
        """
        self.num_actions = num_actions
        self.t_max = t_max
        self.n_min = n_min
        self.n_init = n_init
        self.p = p
        # TODO: complete.
        raise NotImplementedError

    def act(self, t: int) -> int:
        """
        Method that return the action to perform at timestep t.

        :param t: The timestep.
        :return: The action.
        """
        # TODO: complete.
        raise NotImplementedError

    def learn(self, t: int, reward: float) -> None:
        """
        Learning method using the fact that at timestep t the agent got a specific reward.

        :param t: The timestep.
        :param reward: The reward
        """
        # TODO: complete.
        raise NotImplementedError

    def greedy_action(self) -> int:
        """
        Return the action of the best sequence. If there are no sequences of length bigger than n_min, the returned
        action should be -1.
        :return: The action.
        """
        # TODO: complete.
        raise NotImplementedError
