import sys
import program.luminance as luminance
import matplotlib.pyplot as plt

from program.picture import Picture


if __name__ == "__main__":
  pic = Picture(sys.argv[1])

  for col in range(pic.width()):
    for row in range(pic.height()):
      pixel = pic.get(col, row)
      gray = luminance.to_gray(pixel)
      pic.set(col, row, gray)

  pic.draw()

  plt.show(pic._fig)
