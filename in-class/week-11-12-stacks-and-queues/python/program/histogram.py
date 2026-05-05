import numpy as np
import sys
import matplotlib.pyplot as plt


plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})


class Histogram(object):
  def __init__(self, n):
    self._freq = [0 for i in range(n+1)]

  def add_data_point(self, i):
    self._freq[i] += 1

  def draw(self):
    fig, ax = plt.subplots()
    self._fig = fig
    self._ax = ax
    
    # draw using matplotlib
    bar_handler = self._ax.bar(
      list(range(len(self._freq))),
      self._freq)

    self._bar_handler = bar_handler


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

  plt.show(histogram._fig)


if __name__ == "__main__": _main()