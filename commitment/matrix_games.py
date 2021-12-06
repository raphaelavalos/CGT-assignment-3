from typing import Iterable


class MatrixGame:
    """
    Matrix Game environment.
    """

    def __init__(self):
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
