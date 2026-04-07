import sys
import scipy.stats as sc_stats
import numpy as np

def invert(f, y, low, high, delta=1e-8):
  mid = (low + high) / 2.0
  if (high - low) < delta:
    return mid
  if f(mid) > y:
    return invert(f, y, low, mid, delta)
  else:
    return invert(f, y, mid, high, delta)

def _main():
  y = float(sys.argv[1])
  # x = invert(sc_stats.norm.cdf, y, -8.0, 8.0)
  x = invert(lambda p: 1./p**2, y, 0.01, 1)

  print(f"{x:.3f}")

if __name__ == "__main__": _main()