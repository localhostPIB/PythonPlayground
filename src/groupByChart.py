import random

from plotly import graph_objects as go
import plotly.express as px
import plotly.io as pio


list = list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']

list2= [10, 15, 5]

fig = go.Figure()

randomlist = []
test = []
for _ in range(0, 17):
	n = random.randint(1, 10)
	randomlist.append(n)
	
data = [dict(
  type = 'scatter',
  x = list,
  y = randomlist,
  mode = 'markers',
  transforms = [dict(
    type = 'groupby',
    groups = list
  )]
)]

fig_dict = dict(data=data)
pio.show(fig_dict, validate=False)
