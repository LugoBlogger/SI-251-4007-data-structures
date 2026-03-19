import sys
import matplotlib.pyplot as plt

from program.color import Color
from matplotlib.patches import Rectangle

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})

def create_rect(xc, yc, r, color, ax=None):

  square = Rectangle((xc - r, yc - r), 2*r, 2*r, 
    color=(color.get_red()/255, color.get_green()/255, color.get_blue()/255))
  ax.add_artist(square)


if __name__ == "__main__":
  r1 = int(sys.argv[1])
  g1 = int(sys.argv[2])
  b1 = int(sys.argv[3])
  c1 = Color(r1, g1, b1)

  r2 = int(sys.argv[4])
  g2 = int(sys.argv[5])
  b2 = int(sys.argv[6])
  c2 = Color(r2, g2, b2)

  # -- make a square with matplotlib.patches.Rectangle
  # the center is at (xc, yc) and sides 2r

  fig, ax = plt.subplots()

  create_rect(.25, .5, .2, c1, ax=ax)
  create_rect(.25, .5, .1, c2, ax=ax)

  create_rect(.75, .5, .2, c2, ax=ax)
  create_rect(.75, .5, .1, c1, ax=ax)

  ax.set_aspect("equal")

  plt.show(fig)
