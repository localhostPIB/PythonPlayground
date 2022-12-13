import pygal
import random
from pygal.style import Style


list = list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']


randomlist = []
test = []
for _ in range(0,4):
	n = random.randint(1, 1000)
	randomlist.append(n)
	

treemap = pygal.Treemap(width=1920, height=1080, tooltip_font_size=3, legend_at_bottom=True)
treemap.title = 'Treemap'
treemap.range = [0, 1000]

for i, skill in enumerate(list):
	treemap.add(skill, randomlist[i])



treemap.render_to_file('newchart.svg')  
