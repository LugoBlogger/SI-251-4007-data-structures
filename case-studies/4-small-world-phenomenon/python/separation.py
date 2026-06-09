import sys

from graph import Graph
from pathfinder import PathFinder

def _main():
  filename = sys.argv[1]
  delimiter = sys.argv[2]
  g = Graph(filename=filename, delimiter=delimiter)
  print(g)

  s = sys.argv[3]
  pf = PathFinder(g, s)

  while True:
    t = input()
    if t == "":
      break
    else:
      if pf.has_path_to(t):
        distance = pf.distance_to(t)
        for v in pf.path_to(t):
          print(f"  " + v)
        print(f"distance: {distance}")


if __name__ == "__main__":
  _main()