import numpy as np
import sys

class Charge(object):
  def __init__(self, x0, y0, q0):
    self._rx = x0
    self._ry = y0
    self._q = q0

  def potential_at(self, x, y):
    COULOMB = 8.99e09
    dx = x - self._rx
    dy = y - self._ry
    r = np.sqrt(dx*dx + dy*dy)
    if r == 0.0: return float("inf")
    return COULOMB * self._q / r

  def __str__(self):
    result = f"{self._q} at ({self._rx}, {self._ry})"
    return result


def _main():
  x = float(sys.argv[1])
  y = float(sys.argv[2])
  c = Charge(.51, .63, 21.3)

  print(c)
  print(c.potential_at(x, y))


if __name__ == "__main__":
  _main()