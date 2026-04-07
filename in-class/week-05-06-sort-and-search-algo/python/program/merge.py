# Logs
# - [2026/03/28] 
#   Implement mergesort
# 
# TODO
# - fix the space to have the same result like in Program 4.2.6

import sys

def _merge(a, low, mid, high, aux):
  n = high - low
  i = low
  j = mid
  for k in range(n):
    if i == mid: 
      aux[k] = a[j]
      j += 1

    elif j == high:
      aux[k] = a[i]
      i += 1

    elif a[j] < a[i]:
      aux[k] = a[j]
      j += 1

    else:
      aux[k] = a[i]
      i += 1

  a[low:high] = aux[0:n]

  # Answer to Exercise 4.2.8
  # The hint is to look at the trace of recursive mergesort calls
  # if low == 0:
  #   print(" ".join(["   "]*low), end="")
  # else:
  #   print(" ".join(["   "]*low), end=" ")
  # print(" ".join(a[low:high]))

def _sort(a, low, high, aux):
  n = high - low
  
  # -- the length subarray is 0 or 1. It means that the array is already sorted
  if n <= 1: 
    return 

  # print(a, low, high, aux)
  mid = (low + high) // 2

  # print(" ".join(["   "]*(mid-low-1)))
  _sort(a, low, mid, aux)
  _sort(a, mid, high, aux)
  _merge(a, low, mid, high, aux)


def sort(a):
  n = len(a)
  aux = [None] * n
  _sort(a, 0, n, aux)


def _main():
  filename = sys.argv[1]
  with open(filename, 'r') as fp:
    data = fp.readlines()

  data = " ".join(data).split()
  data = [word.strip() for word in data]

  # print(" ".join(data))

  sort(data)

  print(" ".join(data))


if __name__ == "__main__": _main()