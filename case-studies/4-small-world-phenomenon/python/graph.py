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
        for i in range(1, len(names)):
          self.add_edge(names[0], names[i])

  def __str__():
    pass

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
    pass

  def count_e(self):
    pass

  def degree(self, v):
    pass

  def has_vertex(self, v):
    pass

  def has_edge(self, v, w):
    pass


  def vertices(self):
    pass

  def adjacent_to(self, v):
    pass


def _main():
  filename = sys.argv[1]
  graph = Graph(filename=filename)

  print(graph)


if __name__ == "__main__":
  _main()