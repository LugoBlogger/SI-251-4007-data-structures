import sys

def _search(key, a, low, high):
  if high <= low: return - 1      # Not found.
  mid = (low + high) // 2
  if a[mid] > key:
    return _search(key, a, low, mid)
  elif a[mid] < key:
    return _search(key, a, mid+1, high)
  else:
    return mid


def search(key, a):
  return _search(key, a, 0, len(a))


def _main():
  filename = sys.argv[1]
  with open(filename, "r") as fp:
    data_sorted_arr = fp.readlines()

  data_sorted_arr = [email.strip() for email in data_sorted_arr]


  filename = sys.argv[2]
  with open(filename, "r") as fp:
    data_keys = fp.readlines()
  
  data_keys = [email.strip() for email in data_keys]

  # print(data_keys) 
  # print(data_sorted_arr) 

  for key in data_keys:
    if search(key, data_sorted_arr) < 0:
      print(key)


if __name__ == "__main__": _main()