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