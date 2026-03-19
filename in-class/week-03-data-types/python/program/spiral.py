import numpy as np
import sys
import matplotlib.pyplot as plt

from turtle import Turtle

n = int(sys.argv[1])
wraps = int(sys.argv[2])
decay = float(sys.argv[3])
angle = 360.0 / n

step = np.sin(np.radians(angle/2.0))
turtle = Turtle(0.5, 0, angle/2.0)

pen_radius = 2.0

for i in range(wraps * n):
  step /= decay
  turtle.go_forward(step)
  turtle.turn_left(angle)

turtle.draw()

# set pen radius in here with matplotlib line plot
turtle._line_handler[0].set_linewidth(pen_radius)

# show figure
plt.show(turtle._fig)