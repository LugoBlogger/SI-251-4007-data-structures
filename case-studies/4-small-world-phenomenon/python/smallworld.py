import sys

from graph import Graph
from pathfinder import PathFinder


def average_degree(graph):
  return 2.0 * graph.count_e() / graph.count_v()

def average_path_length(graph):
  total = 0
  for v in graph.vertices():
    pf = PathFinder(graph, v)
    for w in graph.vertices():
      total += pf.distance_to(w)

  return 1.0 * total / (graph.count_v() * (graph.count_v() - 1))


def clustering_coefficient(graph):
  total = 0
  for v in graph.vertices():
    possible = graph.degree(v) * (graph.degree(v) - 1)
    actual = 0
    for u in graph.adjacent_to(v):
      for w in graph.adjacent_to(v):
        if graph.has_edge(u, w):
          actual += 1
    
    if possible > 0:
      total += 1.0 * actual / possible

  return total / graph.count_v()


def _main():
  # From Exercise 4.5.21
  filename = sys.argv[1]
  delimiter = sys.argv[2]
  g = Graph(filename=filename, delimiter=delimiter)
  
  num_of_vertices = g.count_v()
  num_of_edges = g.count_e()
  units = "vertices"
  if num_of_vertices == 1:
    units = "vertex"
  print(f"{num_of_vertices} {units}, ", end="")
  
  units = "edges"
  if num_of_edges == 1:
    units = "edge"
  print(f"{num_of_edges} {units}")

  print(f"average degree         = {average_degree(g):.4f}")
  print(f"average path length    = {average_path_length(g):.4f}")
  print(f"clustering coefficient = {clustering_coefficient(g):.4f}")



if __name__ == "__main__": _main()
