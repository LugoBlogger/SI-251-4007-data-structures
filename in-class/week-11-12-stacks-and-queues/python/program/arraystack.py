import sys

class Stack(object):
  def __init__(self):
    self._a = []

  def is_empty(self):
    return len(self._a) == 0

  def __len__(self):
    return len(self._a)

  def push(self, item):
    self._a += [item]

  def pop(self):
    return self._a.pop()


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
      print(f"{stack.pop()} ", end="")
  print()

if __name__ == "__main__": _main()