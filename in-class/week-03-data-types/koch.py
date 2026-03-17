import sys
import matplotlib.pyplot as plt

from turtle import Turtle


def koch(n, step, turtle):
  if n == 0:
    turtle.go_forward(step)
    return

  koch(n-1, step, turtle)
  turtle.turn_left(60.0)

  koch(n-1, step, turtle)
  turtle.turn_left(-120.0)

  koch(n-1, step, turtle)
  turtle.turn_left(60.0)

  koch(n-1, step, turtle)


n = int(sys.argv[1])

pen_radius = 1.

step = 3.0 ** n
turtle = Turtle(0.0, 0.0, 0.0)
koch(n, step, turtle)

turtle.draw()

# set pen radius in here with matplotlib line plot
turtle._line_handler[0].set_linewidth(pen_radius)

# show figure
plt.show(turtle._fig)