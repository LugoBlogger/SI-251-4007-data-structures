# Logs
# - [2026/03/18]
#   To make it faster, we have to add another method .draw()
#   after we upate all xdata, ydata

import sys
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})


class Turtle(object):
  def __init__(self, x0, y0, a0):
    self._x = x0
    self._y = y0
    self._angle = a0

    self._xdata = []
    self._ydata = []
    
  def turn_left(self, delta):
    self._angle += delta

  def go_forward(self, step):
    old_x = self._x
    old_y = self._y
    self._x += step * np.cos(np.radians(self._angle))
    self._y += step * np.sin(np.radians(self._angle))

    # -- update xdata and ydata
    xdata = self._xdata.copy()
    ydata = self._ydata.copy()
    # print(xdata)
    # print(ydata)
    
    if len(xdata) == 0:
      xdata = [old_x, self._x]
      ydata = [old_y, self._y]
    else:
      xdata = np.concatenate((xdata, [self._x]))
      ydata = np.concatenate((ydata, [self._y]))

    self._xdata = xdata.copy()
    self._ydata = ydata.copy()

  def draw(self):
    fig, ax = plt.subplots()

    self._fig = fig
    self._ax = ax

    line_handler = self._ax.plot(self._xdata, self._ydata)

    self._ax.set_aspect("equal")
    self._line_handler = line_handler


def _main():
  n = int(sys.argv[1])
  step = np.sin(np.radians(180.0/n))
  turtle = Turtle(.5, .0, 180.0/n)
  for i in range(n):
    turtle.go_forward(step)
    turtle.turn_left(360.0/n)

  turtle.draw()
  plt.show(turtle._fig)


if __name__ == "__main__": _main()
