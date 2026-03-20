import sys

from program.vector import Vector

class Sketch(object):
  def __init__(self, text, k, d):
    freq = [0 for i in range(d)]
    for i in range(len(text) - k):
      kgram = text[i:i+k]
      freq[hash(kgram) % d] += 1

    vector = Vector(freq)
    self._sketch = vector.direction()

  def similar_to(self, other):
    return self._sketch.dot(other._sketch)

  def __str__(self):
    return str(self._sketch)


def _main():
  text_filename = sys.argv[3]
  k = int(sys.argv[1])
  d = int(sys.argv[2])

  with open(text_filename, "r") as fp:
    text = "".join(fp.readlines())

  # print(text)
  sketch = Sketch(text, k, d)
  print(sketch)


if __name__ == "__main__": _main()