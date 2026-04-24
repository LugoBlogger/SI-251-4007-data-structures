import sys
import numpy as np
import program.threesum as threesum

from program.stopwatch import Stopwatch

def time_trial(n):
  rng = np.random.default_rng()
  a = rng.uniform(-1_000_000, 1_000_000, size=n)
  watch = Stopwatch()
  count, triples = threesum.count_triples(a)
  return watch.elapsed_time()

def _main():
  n = int(sys.argv[1])
  n_max = int(sys.argv[2])

  while True:
    previous = time_trial(n // 2)
    current = time_trial(n)
    ratio = current / previous
    print(f"{n:7d} {ratio:4.2f}")

    n *= 2
    if n > n_max: 
      break


if __name__ == "__main__": _main()