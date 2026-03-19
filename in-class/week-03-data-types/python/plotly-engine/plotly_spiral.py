import numpy as np
import sys

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

turtle._fig.update_traces(line=dict(width=pen_radius))
turtle._fig.show()