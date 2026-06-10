import sys
import smallworld

from graph import Graph


def _main():
  filename = sys.argv[1]
  delimiter = sys.argv[2]

  g = Graph()

  with open(filename, "r") as fp:
    lines = fp.readlines()

  for line in lines:
    names = line.split(delimiter)
    for i in range(1, len(names)):
      for j in range(i+1, len(names)):
        g.add_edge(names[i], names[j])

  # print(g)
  degree = smallworld.average_degree(g)
  length = smallworld.average_path_length(g)
  cluster = smallworld.clustering_coefficient(g)

  print(f"number of vertices     = {g.count_v():3d}")
  print(f"average degree         = {degree:7.3f}")
  print(f"average path length    = {length:7.3f}")
  print(f"clustering coefficient = {cluster:7.3f}")




if __name__ == "__main__": _main()