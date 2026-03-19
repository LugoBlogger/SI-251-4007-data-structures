import sys
import numpy as np
import matplotlib.pyplot as plt

from program.color import Color
from program.picture import Picture
from program.complex import Complex
from program.utils import check_file

from tqdm import tqdm 

def mandel(z0, limit):
  z = z0
  for i in range(limit):
    if abs(z) > 2.0: return i
    z = z*z + z0
  return limit

n = int(sys.argv[1])
xc = float(sys.argv[2])
yc = float(sys.argv[3])
size = float(sys.argv[4])

filename = "./data/" + f"mandelbrot__{n}__{xc}__{yc}___{size}".replace(".", "_") \
  + ".npz"
# print(filename)
is_exist = check_file(filename)


pic = Picture(n, n)

col_row_arr = [[col, row] for col in range(n)
                for row in range(n)]

if is_exist:
  data = np.load(filename, allow_pickle=True)
  pic._surface = data["img_rgb"].copy()
else:
  for col_row in tqdm(col_row_arr):
    col, row = col_row
    x0 = xc - size/2 + size*col/n
    y0 = yc - size/2 + size*row/n
    z0 = Complex(x0, y0)
    gray = 255 - mandel(z0, 255)
    # print(gray)
    color = Color(gray, gray, gray)
    pic.set(col, n-1-row, color)

  # -- save the array
  img_rgb = pic._surface
  np.savez(filename, img_rgb=img_rgb)

img_rgb = np.transpose(pic._surface, [1, 0, 2])
pic._surface = img_rgb

pic.draw()

plt.show(pic._fig)