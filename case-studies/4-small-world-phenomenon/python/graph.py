import sys

class Graph(object):
  def __init__(self, filename=None, delimiter=None):
    self._e = 0
    self._adj = dict()
    if filename is not None:
      with open(filename, "r") as fp:
        lines = fp.readlines()

      for line in lines:
        names = line.split(delimiter)
        names = [name.strip() for name in names]
        for i in range(1, len(names)):
          self.add_edge(names[0], names[i])

  def __str__(self):
    s = ""
    for v in self.vertices():
      s += v + ": "
      for w in self.adjacent_to(v):
        s += w + " "
      s += "\n"
    return s

  def add_edge(self, v, w):
    if not self.has_vertex(v):
      self._adj[v] = set()
      
    if not self.has_vertex(w):
      self._adj[w] = set()

    if not self.has_edge(v, w):
      self._e += 1
      self._adj[v].add(w)
      self._adj[w].add(v)
    

  def count_v(self):
    return len(self._adj)

  def count_e(self):
    return self._e

  def degree(self, v):
    return len(self._adj[v])

  def has_vertex(self, v):
    return v in self._adj

  def has_edge(self, v, w):
    return w in self._adj[v]

  def vertices(self):
    return iter(self._adj)

  def adjacent_to(self, v):
    return iter(self._adj[v])


def _main():
  filename = sys.argv[1]
  graph = Graph(filename=filename)

  print(graph)


if __name__ == "__main__":
  _main()