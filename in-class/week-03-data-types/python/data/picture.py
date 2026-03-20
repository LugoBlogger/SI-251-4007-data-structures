# Logs
# - [2026/03/17]   
#   Use imshow from matplotlib instead of pygame
#   
#   

import numpy as np
import program.color as color
import matplotlib.pyplot as plt

from PIL import Image

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams.update({
  'font.size': 16, 
  'grid.alpha': 0.25})

_DEFAULT_WIDTH = 512
_DEFAULT_HEIGHT = 512

class Picture(object):
  """A Picture object moduls an image. It is initialized such that
  it has a given width and height and contains all black pixel.
  Subsequently you can load an image from a given JPG or PNG file."""

  def __init__(self, arg1=None, arg2=None) :
    """If both arg1 and arg2 are None, then construct self such that it is all 
    black with _DEFAULT_WIDTH and height _DEFAULT_HEIGHT. 
    If arg1 is not None and arg2 is None, then construct self by reading from 
    the file whose name is arg1.
    If neither arg1 nor arg2 is None, then construct self such that it is 
    all black with width arg1 and height arg2."""
    if (arg1 is None) and (arg2 is None):
      maxW = _DEFAULT_WIDTH
      maxH = _DEFAULT_WIDTH

      img_rgb = np.zeros((maxH, maxW, 3), np.uint8)
      self._surface = img_rgb

    elif (arg1 is not None) and (arg2 is None):
      file_name = arg1
      try:
        
        img_rgb = np.array(Image.open(file_name))
        self._surface = img_rgb

      except FileNotFoundError:
        raise IOError()

    elif (arg1 is not None) and (arg2 is not None):
      maxW = arg1
      maxH = arg2
      img_rgb = np.zeros((maxH, maxW, 3), np.uint8)
      
      self._surface = img_rgb


    else:
      raise ValueError()


  def draw(self):
    fig, ax = plt.subplots()
    self._fig = fig
    self._ax = ax

    imshow_handler = self._ax.imshow(self._surface) 

    ax.set_aspect("equal")
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    
    self._imshow_handler = imshow_handler


  def save(self, f):
    """Save self to the file whose name is f."""
    self._fig.savefig(f)

  def width(self):
    """Return the width of self."""
    return self._surface.shape[1]

  def height(self):
    """Return the height of self."""
    return self._surface.shape[0]

  def get(self, x, y):
    """Return the color of self at location (x, y)."""
    data_color = self._surface[y, x, :]
    return color.Color(*data_color)

  def set(self, x, y, c):
    """Set the color of self at location (x, y) to c."""
    data_color = np.array([c.get_red(), c.get_green(), c.get_blue()], dtype=np.uint8)
    # # print(data_color)
    # im_data = self._surface.copy()
    # # print(im_data[x, y, :])
    # im_data[x, y, :] = data_color
    # im_data = im_data.astype(int)   # imshow needs integers 0..255
    # self._surface = im_data.copy()
    self._surface[y, x, :] = data_color.copy()

  

  