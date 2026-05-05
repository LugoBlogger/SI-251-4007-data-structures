import sys
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})

from linkedqueue import Queue
from histogram import Histogram


def _main(lambd, mu, t_max):
  queue = Queue()

  rng = np.random.default_rng()
  next_arrival = rng.exponential(1/lambd)
  next_service = next_arrival + rng.exponential(1/mu)

  max_time = 60
  histogram = Histogram(max_time+1)
  t = 0
  while True:
    while next_arrival < next_service:
      queue.enqueue(next_arrival)
      next_arrival += rng.exponential(1/lambd)

    arrival = queue.dequeue()
    wait = next_service - arrival
    histogram.add_data_point(min(max_time, int(round(wait))))

    if queue.is_empty():
      next_service = next_arrival + rng.exponential(1/mu)
    else:
      next_service = next_service + rng.exponential(1/mu)

    t += 1
    if t > t_max:
      break

  histogram.draw()

  # -- draw the average number of customer. We cannot do this
  # because we simulate only finite numbers of queue
  # histogram._ax.axhline(np.mean(histogram._freq))
  # avg_num_cust = lambd/(mu - lambd)
  # sim_avg_num_cust = np.mean(histogram._freq[:-1])
  # print(avg_num_cust, sim_avg_num_cust)
  # histogram._ax.axhline(avg_num_cust)


  histogram._fig.set_size_inches(12, 5)
  histogram._ax.set_xlabel("wait time (minutes)")
  histogram._ax.set_ylabel("num. of customer")
  histogram._ax.grid("on")
  xticks = np.arange(0, max_time+1, 10)
  labels = [f"{i}" for i in range(0, max_time+1, 10)]
  labels[-1] = f"{max_time}+"
  histogram._ax.set_xticks(xticks)
  histogram._ax.set_xticklabels(labels)

  plt.show(histogram._fig) 




if __name__ == "__main__":
  # we do not use variable name lambda, because lambda is reserved
  # keyword in Python
  lambd = float(sys.argv[1])
  mu = float(sys.argv[2])
  t_max = int(sys.argv[3])
  _main(lambd, mu, t_max)