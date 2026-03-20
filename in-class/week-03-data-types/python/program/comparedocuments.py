import sys
import numpy as np
import matplotlib.pyplot as plt

from program.sketch import Sketch
from program.utils import heatmap, annotate_heatmap


plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})


if __name__ == "__main__":
  k = int(sys.argv[1])
  d = int(sys.argv[2])

  file_input = sys.argv[3]
  with open(file_input, "r") as fp:
    filenames = fp.readlines()
  
  filenames = [doc.strip() for doc in filenames]
  n_files = len(filenames)
  prefix = "data/"
  # print(filenames)
  sketches = [None] * n_files
  for i in range(n_files):
    with open(prefix + filenames[i], "r") as fp:
      text = "".join(fp.readlines())
      sketches[i] = Sketch(text, k, d)

  print(f" "*8, end="")
  for i in range(n_files):
    print(f"{filenames[i]:8.4s}", end="")
  print()

  
  similarity = [[0.0 for j in range(n_files)] for i in range(n_files)]
  for i in range(n_files):
    print(f"{filenames[i]:.4s}", end="")
    for j in range(n_files):
      similarity[i][j] = sketches[i].similar_to(sketches[j])
      print(f"{similarity[i][j]:8.2f}", end="")
    print() 

  fig, ax = plt.subplots(figsize=(8, 8))

  # imshow_handler = ax.imshow(similarity)
  
  # # -- Show all ticks and label them with the respective list entries
  # labels = [f"{filename:.4s}" for filename in filenames]
  # ax.set_xticks(range(n_files), labels=labels, 
  #               rotation=45, ha="right", rotation_mode="anchor")
  # ax.set_yticks(range(n_files), labels=labels)

  # # -- Loop over data dimensions and create text annotations.
  # for i in range(n_files):
  #   for j in range(n_files):
  #     ax.text(j, i, f"{similarity[i][j]:.2f}", ha="center", va="center", color="w")

  # ax.set_aspect("equal")

  labels = [f"{filename:.4s}" for filename in filenames]
  im, cbar = heatmap(np.array(similarity), labels, labels, ax=ax, cmap="YlGn", cbarlabel="similarity")
  texts = annotate_heatmap(im, valfmt="{x:.2f}")

  plt.show(fig)


