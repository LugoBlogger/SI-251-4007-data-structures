import sys
import numpy as np
import plotly.graph_objects as go

from turtle import Turtle

n = int(sys.argv[1])
trials = int(sys.argv[2])
step = float(sys.argv[3])

rng = np.random.default_rng()
pen_radius = 1.0

turtles = [0.0 for _ in range(n)]
for i in range(n):
  x = rng.uniform(0.0, 1.0)
  y = rng.uniform(0.0, 1.0)
  turtles[i] = Turtle(x, y, 0.0)

for t in range(trials):
  for i in range(n):
    angle = rng.uniform(0.0, 360.0)
    turtles[i].turn_left(angle)
    turtles[i].go_forward(step)

collect_data = []
for i in range(n):
  collect_data += list(turtles[i]._fig.data)
combined_fig = go.Figure(data=collect_data)

# Alternatively, add them one by one
# for trace in fig2.data:
#     fig1.add_trace(trace)

combined_fig.update_layout(
  autosize=False, 
  xaxis=dict(tickfont_size=20),
  yaxis=dict(tickfont_size=20)
)

combined_fig.update_yaxes(
  scaleanchor='x',
  scaleratio=1
)

combined_fig.show()