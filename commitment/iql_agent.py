import numpy as np


class IQLAgent:
    """
    The agent class for exercise 1.
    """

    def __init__(self,
                 num_actions: int,
                 epsilon_max: float = None,
                 epsilon_min: float = None,
                 epsilon_decay: float = None):
        """
        :param num_actions: Number of actions.
        :param epsilon_max: The maximum epsilon of epsilon-greedy.
        :param epsilon_min: The minimum epsilon of epsilon-greedy.
        :param epsilon_decay: The decay factor of epsilon-greedy.
        """
        self.q_table = np.zeros((num_actions,))
        self.count = np.zeros((num_actions,), dtype=int)
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.epsilon_max = epsilon_max
        self.epsilon = epsilon_max

    def greedy_action(self) -> int:
        """
        Return the greedy action.

        :param observation: The observation.
        :return: The action.
        """
        # TODO: complete.
        raise NotImplementedError

    def act(self, training: bool = True) -> int:
        """
        Return the action.

        :param training: Boolean flag for training.
        :return: The action.
        """
        # TODO: complete.
        raise NotImplementedError

    def learn(self, act: int, rew: float) -> None:
        """
        Update the Q-Value.

        :param obs: The observation.
        :param act: The action.
        :param rew: The reward.
        """
        # TODO: complete.
        raise NotImplementedError
