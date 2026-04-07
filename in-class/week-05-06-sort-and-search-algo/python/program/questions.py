import sys

def search(low, high, counter):
  if (high - low) == 1:
    return low
  mid = (high + low) // 2
  stat = input(f"({counter:03d}) Greater than or equal to {mid}? ")
  if stat.lower() == "true":
    stat = True
  elif stat.lower() == "false":
    stat = False
  else:
    return print(f"Your input is wrong!")

  if stat:
    return search(mid, high, counter+1)
  else:
    return search(low, mid, counter+1)


def _main():
  k = int(sys.argv[1])
  n = 2 ** k
  print(f"Think of a number between 0 and {n-1}")
  guess = search(0, n, 1)
  print(f"Your number is {guess}")


if __name__ == "__main__": _main()
