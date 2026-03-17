import sys
import numpy as np
import matplotlib.pyplot as plt

from turtle import Turtle

n = int(sys.argv[1])
trials = int(sys.argv[2])
step = float(sys.argv[3])

rng = np.random.default_rng()
pen_radius = 1.0

turtles = [0.0 for _ in range(n)]
for i in range(n):
  x = rng.uniform(0.0, 1.0)
  y = rng.uniform(0.0, 1.0)
  turtles[i] = Turtle(x, y, 0.0)

for t in range(trials):
  for i in range(n):
    angle = rng.uniform(0.0, 360.0)
    turtles[i].turn_left(angle)
    turtles[i].go_forward(step)

data = [
  [turtle._xdata for turtle in turtles],
  [turtle._ydata for turtle in turtles]]

fig, ax = plt.subplots()
for t in range(n):
  line_handler = ax.plot(data[0][t], data[1][t])
  line_handler[0].set_linewidth(pen_radius)
  line_handler[0].set_color("tab:blue")

ax.set_aspect("equal")

plt.show(fig)