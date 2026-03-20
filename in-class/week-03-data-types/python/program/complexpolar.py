import numpy as np

class Complex(object):
  def __init__(self, re=0, im=0):
    self._r = np.hypot(im, re)
    self._theta = np.arctan2(im, re)

  def re(self): return self._r * np.cos(self._theta)
  def im(self): return self._r * np.sin(self._theta)

  def __add__(self, other):
    re = self.re() + other.re()
    im = self.im() + other.im()
    return Complex(re, im)

  def __mul__(self, other):
    c = Complex()
    c._r = self._r * other._r
    c._theta = self._theta + other._theta
    return c

  def __abs__(self): return self.r

  def __str__(self):
    return str(self.re()) + ' + ' + str(self.im()) + 'i'

def _main():
  z0 = Complex(1.0, 1.0)
  z = z0
  z = z*z + z0
  z = z*z + z0
  print(z)


if __name__ == "__main__": _main()