import time
import sys

class Stopwatch(object):
  def __init__(self):
    self._start = time.time()
  
  def elapsed_time(self):
    return time.time() - self._start


def _main():
  n = int(sys.argv[1])

  total_1 = 0.0
  watch_1 = Stopwatch()
  for i in range(1, n+1):
    total_1 += i**2
  time_1 = watch_1.elapsed_time()

  total_2 = 0.0
  watch_2 = Stopwatch()
  for i in range(1, n+1):
    total_2 += i*i
  time_2 = watch_2.elapsed_time()

  print(total_1/total_2)
  print(time_1/time_2)


if __name__ == "__main__": _main()