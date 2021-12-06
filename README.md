# Computational Game Theory - Assignment 3

Here you will find the code for the assignment 3. You have to complete the empty functions/methods based on the signatures and docstring.

WARNING: YOU SHOULD NOT CHANGE THE FUNCTIONS NAMES AND THE FUNCTIONS SHOULD RESPECT THEIR SIGNATURE.

You are free to add functions and methods, however you should properly comment them.

## First task

Complete the `student.py` file with you first and last names and your student number.

## Exercise 1: Frozen Lake

In the directory `frozen_lake` you will find two files: 
- `agents.py`: The main file you need to complete.
- `runner.py`: The training loop is already given to you. You should add your code to create the plots here, and running `python runner.py` should train an agent.

## Exercise 2: Commitment sequences

In the directory `commitment` you wil find five files:
- `matrix_games.py`: The file containing the matrix game environment class.
- `iql_agent.py`: The file for your Independent Q-Learners agents' class.
- `iql_runner.py`: This time you need to code the training loop, use `frozen_lake/runner.py` as inspiration. Running `python iql_runner.py` should train the IQL agents.
- `commitment_agent.py`: The file for your Commitment agents' class.
- `commitment_runner.py`: You should code the training loop. Running `python commitment_runner.py` should train the Commitment agents.

# Change Log:
- You can use `FrozenLake-v1` instead of `FrozenLake-v0`. The code has been updated to load v1 if v0 is not available.
- `frozen_lake/runner.py` line 66 the training flag was not set to False here is the correct line: `cum_rewards_eval[eval_episode] = run_episode(env, agent, False, gamma)`.
- Error in `commitment/commitment_agent.py`: The docstring with the example was not correct, here is the correct version:
```python
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
```

# Additional information:

With regards to the following part in the assignment:
"A plot containing the return of the agent during training and the return at all evaluation times should be included in the report. This plot should be averaged over 20 full training runs with standard deviations as error bars."

You can plot the two plots in one figure. So I would advise you to plot first the (averaged) training returns (with x-values being all episodes), and then again plt.plot(x, y ...) for the evaluation returns, where the x-values are 1000, 2000, 3000, etc., and the y-values are the mean returns of the 32 evaluation episodes (and then average these means again over the 20 runs to calculate the stdevs). Make sure that the averages of your training returns are visible within your stdevs. The easiest way to do this is to make your stdevs more transparent in the settings of your plot.

 

