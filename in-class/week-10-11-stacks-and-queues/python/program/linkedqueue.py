import sys

class Queue(object):
  def __init__(self):
    self._first = None
    self._last = None
    self._n = 0

  def is_empty(self):
    return self._first is None

  def enqueue(self, item):
    old_last = self._last
    self._last = _Node(item, None)
    if self.is_empty():
      self._first = self._last
    else:
      old_last.next = self._last
    
    self._n += 1

  def dequeue(self):
    item = self._first.item
    self._first = self._first.next
    if self.is_empty():
      self._last = None

    self._n -= 1
    return item

  def __len__(self):
    return self._n


class _Node(object):
  def __init__(self, item, next):
    self.item = item
    self.next = next


def _main():
  queue = Queue()
  filename = sys.argv[1]
  with open(filename, "r") as fp:
    data = fp.readlines()

  data = [val.strip() for val in data[0].split()]
  # print(data)

  for item in data:
    if item != "-":
      queue.enqueue(item)
    else:
      print(f"{queue.dequeue()} ", end="")

  print()


if __name__ == "__main__": _main()