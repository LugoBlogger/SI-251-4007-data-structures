import graph

from linkedqueue import Queue


class PathFinder(object):
  def __init__(self, graph, s):
    self._dist_to = dict()
    self._edge_to = dict()

    queue = Queue()
    queue.enqueue(s)
    self._dist_to[s] = 0
    self._edge_to[s] = None
    while not queue.is_empty():
      v = queue.dequeue()
      print(f"v: {v}")
      for w in graph.adjacent_to(v):
        if w not in self._dist_to:
          queue.enqueue(w)
          self._dist_to[w] = 1 + self._dist_to[v] 
          self._edge_to[w] = v

  def distance_to(self, v):
    return self._dist_to[v]

  def has_path_to(self, v):
    return v in self._dist_to

  def path_to(self, v):
    path = []
    while v is not None:
      path += [v]
      v = self._edge_to[v]
    return reversed(path)