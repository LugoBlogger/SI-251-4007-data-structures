import sys
import numpy as np
import plotly.graph_objects as go


class Turtle(object):
  def __init__(self, x0, y0, a0):
    self._x = x0
    self._y = y0
    self._angle = a0
    self._fig = go.Figure()

    self._fig.update_layout(
      autosize=False, 
      xaxis=dict(tickfont_size=20),
      yaxis=dict(tickfont_size=20)
    )

    self._fig.update_yaxes(
      scaleanchor='x',
      scaleratio=1
    )

  def turn_left(self, delta):
    self._angle += delta

  def go_forward(self, step):
    old_x = self._x
    old_y = self._y
    self._x += step * np.cos(np.radians(self._angle))
    self._y += step * np.sin(np.radians(self._angle))

    # draw line
    self._fig.add_trace(go.Scatter(
      x=[old_x, self._x], 
      y=[old_y, self._y], 
      mode='lines', 
      line=dict(color='blue'),
      showlegend=False
    ))


def _main():
  n = int(sys.argv[1])
  step = np.sin(np.radians(180.0/n))
  turtle = Turtle(.5, .0, 180.0/n)
  for i in range(n):
    turtle.go_forward(step)
    turtle.turn_left(360.0/n)

  turtle._fig.show()


if __name__ == "__main__": _main()
