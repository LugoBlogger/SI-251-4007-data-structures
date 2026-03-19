import sys

from program.color import Color

def luminance(c):
  red = c.get_red()
  green = c.get_green()
  blue = c.get_blue()
  return .299*red + .587*green + .114*blue

def to_gray(c):
  y = int(round(luminance(c)))
  return Color(y, y, y)

def are_compatible(c1, c2):
  return abs(luminance(c1) - luminance(c2)) > 128.0

def _main():
  r1 = int(sys.argv[1])
  g1 = int(sys.argv[2])
  b1 = int(sys.argv[3])

  r2 = int(sys.argv[4])
  g2 = int(sys.argv[5])
  b2 = int(sys.argv[6])

  c1 = Color(r1, g1, b1)
  c2 = Color(r2, g2, b2)

  print(are_compatible(c1, c2))


if __name__ == "__main__": _main()