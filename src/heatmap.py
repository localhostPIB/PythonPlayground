import random

from plotly import graph_objects as go
import plotly.express as px
import plotly.io as pio


list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']


randomlist = []
test = []

for _ in range(0, 6):
	for _ in range(0, 17):
		n = random.randint(1, 10)
		randomlist.append(n)
	test.append(randomlist)
	randomlist = []


fig = go.Figure(data=go.Heatmap(z=test, x=list,y=[1,2,3,4,5,6], texttemplate="%{text}", textfont={"size":10}))
fig.update_layout(title="xyz",yaxis={"title": 'Year'}, xaxis={"title": 'Skills',"tickangle": 45}, )
fig.show()
