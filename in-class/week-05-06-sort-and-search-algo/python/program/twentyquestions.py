# Logs
# - [2026/03/26]
#   Program 1.5.2 Interactive user input (twentyquestions.py)
#   This program will ask you to guess a number between 1 and 1,000,000 (inclusively)
#   and you have a task at least no more than twenty questions to guess it

import numpy as np
import sys

def _main():
  RANGE = 1_000_000

  rng = np.random.default_rng()
  secret = rng.integers(1, RANGE + 1)
  print(f"I am thinking of a secret number between 1 and {RANGE:,}")

  guess = 0
  counter = 1
  while guess != secret:
    # Solicit one guess and provide one answer
    guess = input(f"({counter:03d}) What is your guess? ")
    guess = int(guess)

    if (guess < secret): print(f"Too low")
    elif (guess > secret): print(f" Too high")
    else: print(f"You win!")
    counter += 1


if __name__ == "__main__": _main()