import random

from plotly import graph_objects as go
import plotly.express as px


list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']


randomlist = []
test = []
for _ in range(0, 17):
	n = random.randint(1, 10)
	randomlist.append(n)
	#test.append(randomlist)
	#randomlist = []
	

fig = go.Figure(go.Funnel(y = list, x = randomlist))

fig.show()
