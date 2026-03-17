import sys
import numpy as np
import matplotlib.pyplot as plt

from turtle import Turtle

trials = int(sys.argv[1])
step = float(sys.argv[2])

rng = np.random.default_rng()
pen_radius = 1.0

turtle = Turtle(0.5, 0.5, 0.0)
for t in range(trials):
  angle = rng.uniform(0.0, 360)
  turtle.turn_left(angle)
  turtle.go_forward(step)

turtle.draw()

# set pen radius in here with matplotlib line plot
turtle._line_handler[0].set_linewidth(pen_radius)

plt.show(turtle._fig)

