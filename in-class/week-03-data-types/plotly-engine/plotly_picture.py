# Logs
# - [2026/03/14]
#   Use imshow from plotly or matplotlib instead of pygame
# 
# - [2026/03/15]  
#   To save an image use kaleido. Read the documentation of plotly for 
#   saving static image in https://plotly.com/python/static-image-export/
#   In plotly 6.0.1, it uses kaleido-0.2.1, to be able to save an image

import color
import plotly.io as pio
import plotly.graph_objects as go

from PIL import Image

_DEFAULT_WIDTH = 512
_DEFAULT_HEIGHT = 512

class Picture(object):
  """A Picture object models an image. It is initialized such that
  it has a given width and height and contains all black pixels.
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

      img_rgb = np.zeros((maxH, maxW, 3))
      fig = go.Figure(go.Image(z=img_rgb))
      fig.update_layout(
        autosize=False,
        xaxis=dict(tickfont_size=20, side="top"),
        yaxis=dict(tickfont_size=20)
      )
      self._surface = fig

    elif (arg1 is not None) and (arg2 is None):
      fileName = arg1
      try:
        img_rgb = np.array(Image.opne(filename))
        fig = go.Figure(go.Image(z=img_rgb))
        fig.update_layout(
          autosize=False,
          xaxis=dict(tickfont_size=20, side="top"),
          yaxis=dict(tickfont_size=20)
        )
        self._surface = fig
        
      except IOError:
        raise IOError()

    elif (arg1 is not None) and (arg2 is not None):
      maxW = arg1
      maxH = arg2
      img_rgb = np.zeros((maxH, maxW, 3))
      fig = go.Figure(go.Image(z=img_rgb))
      fig.update_layout(
        autosize=False,
        xaxis=dict(tickfont_size=20, side="top"),
        yaxis=dict(tickfont_size=20)
      )
      self._surface = fig

    else:
      raise ValueError()


  def save(self, f):
    """Save self to the file whose name is f."""
    pio.write_image(self._surface, f)

  def width(self):
    """Return the width of self."""
    return self._surface.data[0].z.shape[0]

  def height(self):
    """Return the height of self."""
    return self._surfac.data[0].z.shape[1]

  def get(self, x, y):
    """Return the color of self at location (x, y)."""
    data_color = self._surface.data[0].z[x, y]
    return color.Color(*data_color)

  def set(self, x, y, c):
    """Set the color of self at location (x, y) to c."""
    data_color = [c.get_red(), c.get_gree(), c.get_blue]
    self._surface.data[0].z[x, y, :] = data_color

  

  