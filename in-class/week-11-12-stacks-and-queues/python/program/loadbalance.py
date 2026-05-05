import sys
import numpy as np
import matplotlib.pyplot as plt

from linkedqueue import Queue
from randomqueue import RandomQueue

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})

def _main(m, n, t):

  # -- create an instance of RandomQueue for m servers
  servers = RandomQueue()
  for i in range(m):
    servers.enqueue(Queue())

  # -- add each items to a server that has a least number of items
  # t is the number of server that we sampled
  for j in range(n):
    best = servers.sample()
    for k in range(1, t):
      queue = servers.sample()
      if len(queue) < len(best):
        best = queue

    best.enqueue(j)

  # -- find the number of items in each server
  lengths = []
  while not servers.is_empty():
    lengths += [len(servers.dequeue())]

  fig, ax = plt.subplots(figsize=(10, 4))

  ax.bar(np.arange(len(lengths)), lengths)
  ax.set_xlabel("$i$-th server")
  ax.set_ylabel("number of items ($n$)")
  ax.grid("on")
  ax.set_title(f"sample $t = ${t} server(s)")

  plt.show(fig)



if __name__ == "__main__":
  m = int(sys.argv[1])
  n = int(sys.argv[2])
  t = int(sys.argv[3])

  _main(m, n, t)