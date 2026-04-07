import sys

def write_triples(a_triple_str):
  for triple in a_triple_str:
    print(triple) 


def count_triples(a):
  n = len(a)
  count = 0
  a_triple_str = []
  for i in range(n):
    for j in range(i+1, n):
      for k in range(j+1, n):
        if (a[i] + a[j] + a[k]) == 0:
          count += 1
          a_triple_str.append(f"{a[i]:4d} {a[j]:4d} {a[k]:4d}")

  return count, a_triple_str

def _main():
  filename = sys.argv[1]
  with open(filename, "r") as fp:
    n = int(fp.readline())
    a = [0 for _ in range(n)]
    for i in range(n):
      a[i] = int(fp.readline().strip())

  count, triples = count_triples(a)
  print(count)
  write_triples(triples)


if __name__ == "__main__": _main()