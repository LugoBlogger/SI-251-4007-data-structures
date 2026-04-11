import sys
import numpy as np

from arraystack import Stack

def _main(filename): 
  if filename == "":
    input_str = input()
    input_str = input_str.split()
  else:
    with open(filename, "r") as fp:
      input_str = fp.readlines()
      input_str = [val.strip() for val in input_str[0].split()]
    
    # print(input_str)
    print(" ".join(input_str))

  ops = Stack()
  values = Stack()

  for token in input_str:
    if token == "+": ops.push(token)
    elif token == "-": ops.push(token)
    elif token == "*": ops.push(token)
    elif token == "sqrt": ops.push(token)
    elif token == ")":
      op = ops.pop()
      value = values.pop()
      if op == "+": value = values.pop() + value
      elif op == "-": value = values.pop() - value
      elif op == "*": value = values.pop() * value
      elif op == "sqrt": value = np.sqrt(value)
      values.push(value)

    elif token != "(": values.push(float(token))

  print(values.pop())

if __name__ == "__main__": 
  filename = sys.argv[1]
  _main(filename)