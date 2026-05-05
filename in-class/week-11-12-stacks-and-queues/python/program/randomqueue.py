# Exercise 4.3.40

import sys
import numpy as np

class RandomQueue(object):
  def __init__(self):
    self._a = []
    self._seed = 26_05_05
    # self._seed = None
    self._rng = np.random.default_rng(self._seed)

  def is_empty(self):
    return len(self._a) == 0

  def enqueue(self, item):
    self._a += [item]

  def dequeue(self):
    """Remove and return a random item from q (sample without replacement)"""
    idx_random = self._rng.integers(len(self._a))
    # swap the idx_random with the last index
    self._a[idx_random], self._a[-1] = self._a[-1], self._a[idx_random]

    # dequeue the last element
    item = self._a[-1]
    self._a = self._a[:-1]

    return item

  def sample(self) :
    """Return but do not remove a random item from q (sample with replacement)"""
    idx_random = self._rng.integers(len(self._a))
    return self._a[idx_random]
    
  def __len__(self):
    return len(self._a)


def _main():
  """A client that writes a deck of cards in random order"""
  queue = RandomQueue()

  SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

  for suit in SUITS:
    for rank in RANKS:
      queue.enqueue(f"{rank} of {suit}")
  
  while len(queue) > 0:
    print(queue.dequeue())


if __name__ == "__main__": _main()