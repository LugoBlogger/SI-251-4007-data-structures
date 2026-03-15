# Logs
# - [2026/03/14]
#   Use imshow from plotly or matplotlib instead of pygame

import color

import plotly.express as px

_DEFAULT_WIDTH = 512
_DEFAULT_HEIGHT = 512

class Picture(object):
  """A Picture object models an image. It is initialized such that
  it has a given width and height and contains all black pizels.
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
      
      self._surface

  def save(self, f):
    """Save self to the file whose name is f."""
    px.savefig(self._surface, f)

  def width(self):
    """Return the width of self."""
    return self._surface

  def height(self):
    """Return the height of self."""
    return self._surface

  def get(self, x, y):
    """Return the color of self at location (x, y)."""
    pass

  def set(self, x, y, c):
    """Set the color of self at location (x, y) to c."""
    pass

  

  