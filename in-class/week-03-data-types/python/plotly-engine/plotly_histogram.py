import numpy as np
import sys
import plotly.graph_objects as go


class Histogram(object):
  def __init__(self, n):
    self._freq = [0 for i in range(n+1)]
    self._fig = go.Figure()

    self._fig.update_layout(
      autosize=False, 
      xaxis=dict(tickfont_size=20),
      yaxis=dict(tickfont_size=20)
    )

  def add_data_point(self, i):
    self._freq[i] += 1

  def draw(self):
    # draw using plotly.graph_objects
    self._fig.add_trace(go.Bar(
      x=list(range(len(self._freq))),
      y=self._freq,
      # marker_color="indianred"
    ))



def _main():
  n = int(sys.argv[1])
  p = float(sys.argv[2])
  trials = int(sys.argv[3])

  rng = np.random.default_rng()

  histogram = Histogram(n+1)
  for t in range(trials):
    heads = rng.binomial(n, p)
    histogram.add_data_point(heads)

  histogram.draw()

  histogram._fig.show()


if __name__ == "__main__": _main()