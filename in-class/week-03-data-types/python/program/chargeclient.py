import sys

from program.charge import Charge


if __name__ == "__main__":
  x = float(sys.argv[1])
  y = float(sys.argv[2])
  c1 = Charge(.51, .63, 21.3)
  c2 = Charge(.13, .94, 81.9)

  v1 = c1.potential_at(x, y)
  v2 = c2.potential_at(x, y)

  print(f"potential at ({x:.2f}, {x:.2f}) due to")
  print(f"  {c1} and")
  print(f"  {c2}")
  print(f"is {v1+v2:.2e}")