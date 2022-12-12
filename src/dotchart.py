import pygal
import random

dot_chart = pygal.Dot(x_label_rotation=30, show_legend=False)
dot_chart.title = 'Student xyz'
dot_chart.x_labels = ['Year 1', 'Year 2', 'Year 3', 'Year 4']

list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']


randomlist = []
test = []
for _ in range(0, 17):
	randomlist = []
	for _ in range(0, 4):
		n = random.randint(1, 1000)
		randomlist.append(n)
	test.append(randomlist)
	

for i, skill in enumerate(list):
	dot_chart.add(skill, test[i])

dot_chart.render_to_file('newchart.svg')  
