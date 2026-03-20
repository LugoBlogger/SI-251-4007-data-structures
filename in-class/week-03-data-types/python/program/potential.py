import sys
import numpy as np
import matplotlib.pyplot as plt

from program.charge import Charge
from program.color import Color
from program.picture import Picture


if __name__ == "__main__":
  charge_file = sys.argv[1]

  n = 0
  charge_arr = []
  with open(charge_file, "r") as fp:
    data = fp.readlines()
    data = [row.strip() for row in data]
    n = int(data[0])

    for row in data[1:]:
      charge_arr.append(
        Charge(*[float(col) for col in row.split()]))

  # print(n)
  # for charge_indiv in charge_arr:
  #   print(charge_indiv)

  pic = Picture()
  for col in range(pic.width()):
    for row in range(pic.height()):
      x = 1.0 * col / pic.width()
      y = 1.0 * row / pic.height()
      v = 0.0
      for i in range(n):
        v += charge_arr[i].potential_at(x, y)
      v = (255 / 2.0) + (v / 2.0e10)
      if v < 0: gray = 0
      elif v > 255: gray = 255
      else: gray = int(v)
      color = Color(gray, gray, gray)
      pic.set(col, pic.height()-1-row, color)

  # print(pic._surface)
  pic.draw()
  plt.show(pic._fig)