import sys
import numpy as np
import matplotlib.pyplot as plt

from program.color import Color
from program.picture import Picture
from tqdm import tqdm


def blend(c1, c2, alpha):
  r = (1 - alpha) * c1.get_red()   + alpha*c2.get_red()
  g = (1 - alpha) * c1.get_green() + alpha*c2.get_green()
  b = (1 - alpha) * c1.get_blue()  + alpha*c2.get_blue()

  return Color(int(r), int(g), int(b))

  
if __name__ == "__main__":
  source_file = sys.argv[1]
  target_file = sys.argv[2]
  n = int(sys.argv[3])

  source = Picture(source_file)
  target = Picture(target_file)

  width = source.width()
  height = source.height()

  pic = Picture(width, height)
  history_img_src = np.zeros((n+1, *pic._surface.shape), dtype=np.uint8)

  t_col_row = [[t, col, row] for t in range(n+1)
                for col in range(width)
                  for row in range(height)]
  
  for t, col, row in tqdm(t_col_row):
    c_0 = source.get(col, row)
    c_n = target.get(col, row)
    alpha = 1.0 * t / n
    data_color = blend(c_0, c_n, alpha)
    history_img_src[t, row, col, :] = [
      data_color.get_red(), data_color.get_green(), data_color.get_blue()]

  # -- draw into nrows x 5 axes
  nrows = (n+1)  // 5
  nrows += 1 if (n+1) % 5 != 0 else 0
  fig, axes = plt.subplots(nrows=nrows, ncols=5, figsize=(2*5, 2*nrows),
    sharex=True, dpi=200)
  axes = axes.flatten()

  for idx, img in enumerate(history_img_src):
    axes[idx].imshow(img)
    axes[idx].set_aspect("equal")
    axes[idx].axis("off")

  plt.show(fig)


