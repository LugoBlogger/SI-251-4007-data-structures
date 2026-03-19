import sys
import plotly.graph_objects as go

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

# set pen radius in here with plotly.graph_objects
turtle._fig.update_traces(line=dict(width=pen_radius))

# show figure
turtle._fig.show()