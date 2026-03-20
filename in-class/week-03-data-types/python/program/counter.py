import sys
import numpy as np


class Counter(object):
  def __init__(self, id, max_count):
    self._name = id
    self._max_count = max_count
    self._count = 0

  def increment(self):
    if self._count < self._max_count:
      self._count += 1

  def value(self):
    return self._count

  def __str__(self):
    return f"{self._name}: {self._count:,}"


def _main():
  rng = np.random.default_rng()
  n = int(sys.argv[1])
  p = float(sys.argv[2])
  heads = Counter("Heads", n)
  tails = Counter("Tails", n)
  for i in range(n):
    if rng.binomial(n=1, p=p): 
      heads.increment()
    else:
      tails.increment()

  print(heads)
  print(tails)

if __name__ == "__main__": _main()