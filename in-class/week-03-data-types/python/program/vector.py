import numpy as np

class Vector(object):
  def __init__(self, a):
    self._coords = a[:]
    self._n = len(a)

  def __add__(self, other):
    result = [0 for i in range(self._n)]
    for i in range(self._n):
      result[i] = self._coords[i] + other._coords[i]
    return Vector(result)

  def __sub__(self, other):
    pass

  def dot(self, other):
    result = 0
    for i in range(self._n):
      result += self._coords[i] * other._coords[i]
    return result

  def scale(self, alpha):
    result = [0 for i in range(self._n)]
    for i in range(self._n):
      result[i] = alpha * self._coords[i]
    return Vector(result)

  def direction(self):
    return self.scale(1.0 / abs(self))
  
  def __getitem__(self, i):
    return self._coords[i]

  def __abs__(self):
    return np.sqrt(self.dot(self))
  
  def __len__(self):
    return self._n

  def __str__(self):
    return str(self._coords)


def _main():
  x = Vector([0, 3, 4, 0])
  y = Vector([0, -3, 1, -4])
  print(x, y)

  print(f"x + y =", x + y)
  print(f"3x =", x.scale(3))
  print(f"x.dot(y) =", x.dot(y))
  print(f'|x| =', abs(x))
  print(f"x/|x| =", x.direction())


if __name__ == "__main__": _main()