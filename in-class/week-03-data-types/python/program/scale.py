import sys
import matplotlib.pyplot as plt

from program.picture import Picture


if __name__ == "__main__":
  filename = sys.argv[1]
  w_t = int(sys.argv[2])    # target width
  h_t = int(sys.argv[3])    # target height

  source = Picture(filename)
  target = Picture(w_t, h_t)

  for col_t in range(w_t):
    for row_t in range(h_t):
      col_s = col_t * source.width() // w_t
      row_s = row_t * source.height() // h_t
      target.set(col_t, row_t, source.get(col_s, row_s))

  target.draw()
  plt.show(target._fig)