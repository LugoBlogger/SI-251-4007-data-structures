import sys

from graph import Graph

def _main():
  filename = sys.argv[1]
  delimiter = sys.argv[2]
  g = Graph(filename=filename, delimiter=delimiter)
  # print(g)

  while True:
    v = input()
    if v == "":
      break
    else:
      if g.has_vertex(v):
        for w in g.adjacent_to(v):
          print("  " + w)

if __name__ == "__main__": _main()