import sys


def exchange(a, i, j):
  a[i], a[j] = a[j], a[i]


def sort(a):
  n = len(a)
  for i in range(1, n):
    j = i
    while (j > 0) and (a[j] < a[j-1]):
      exchange(a, j, j-1)
      j -= 1


def _main():
  filename = sys.argv[1]

  with open(filename, "r") as fp:
    data = fp.readlines()

  data = " ".join(data).split()
  data = [word.strip() for word in data]
  # print(data)

  sort(data)
  for s in data:
    print(f"{s}", end=" ")
  print()

if __name__ == "__main__": _main()
