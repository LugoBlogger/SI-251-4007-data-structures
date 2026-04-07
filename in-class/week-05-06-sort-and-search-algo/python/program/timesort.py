import numpy as np

from program.stopwatch import Stopwatch


def time_trials(f, n, trials, rng):
  total = 0.0
  a = [0.0 for i in range(n)]
  for t in range(trials):
    for i in range(n):
      a[i] = rng.random()
    
    watch = Stopwatch()
    f(a)
    total += watch.elapsed_time()

  return total


def doubling_test(f, n_start, trials, n_end, rng):
  n = n_start
  while True:
    prev = time_trials(f, n // 2, trials, rng)
    curr = time_trials(f, n, trials, rng)
    ratio = curr/prev
    print(f"{n:7d} {ratio:4.2f}")
    n *= 2

    if n > n_end:
      break
