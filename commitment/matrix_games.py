from typing import Iterable


class MatrixGame:
    """
    Matrix Game environment.
    """

    def __init__(self):
        """
        :param reward_matrix: Array of shape (nbr_actions_agent_1, ..., nbr_actions_agent_2). The elements of this array
               can be the reward or a callable that returns the reward.
        """
        self.num_agents = 2
        self.num_actions = 3
        raise NotImplementedError

    def act(self, action: Iterable[int]):
        """
        Method to perform an action in the Matrix Game and obtain the associated reward.
        :param action: The joint action.
        :return: The reward.
        """
        raise NotImplementedError
