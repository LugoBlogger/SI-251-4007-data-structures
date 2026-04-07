

class Stack(object):
  def __init__(self):
    self._first = None

  def is_empty(self):
    return self._first is None

  def push(self, item):
    self._first = _Node(item, self._first)

  def pop(self):
    item = self._first.item
    self._first = self._first.next
    return item


class _Node(object):
  def __init__(self, item, next):
    self.item = item
    self.next = next


def _main():
  stack = Stack()
  filename = sys.argv[1]
  with open(filename, "r") as fp:
    data = fp.readlines()

  data = [val.strip() for val in data[0].split()]

  for item in data:
    if item != "-":
      stack.push(item)
    else:
      print(f"{stack.pop} ", end="")
  print()

if __name__ == "__main__": _main()
