import sys

def moves(n, enter):
  if n == 0:
    return

  moves(n-1, True)
  if enter:
    print(f"enter {n}")
  else:
    print(f"exit  {n}")
  moves(n-1, False)


def moves_with_steps(arr, n, n_total, enter):
  """
  We need to keep track the total length, so we add n_total argument
  """
  if n == 0:
    return arr

  arr = moves_with_steps(arr, n-1, n_total, True)

  if enter:
    arr = [n] + arr
    arr.sort()
    arr = arr[::-1]

    arr_str = [f"{val}" for val in arr]
    bin_code = [0] * n_total
    for val in arr:
      bin_code[val-1] = 1
    bin_code = bin_code[::-1]
    bin_code_str = [f"{val}" for val in bin_code]

    print(f"{' '.join(bin_code_str):8s} {' '.join(arr_str):^10s} enter {n}")
  else:
    if n in arr:
      arr.remove(n)

    arr_str = [f"{val}" for val in arr]
    bin_code = [0] * n_total
    for val in arr:
      bin_code[val-1] = 1
    bin_code = bin_code[::-1]
    bin_code_str = [f"{val}" for val in bin_code]
    
    print(f"{' '.join(bin_code_str):8s} {' '.join(arr_str):^10s}  exit {n}")
  
  arr = moves_with_steps(arr, n-1, n_total, False)

  return arr
  

  



def _main():
  n = int(sys.argv[1])
  moves(n, True)


if __name__ == "__main__": _main()