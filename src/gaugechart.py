import pygal
import random
from pygal.style import Style




list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']


randomlist = []
test = []
for _ in range(0,8):
	n = random.randint(1, 1000)
	randomlist.append(n)


gauge_chart = pygal.Gauge(human_readable=True, width=1920, height=1080, tooltip_font_size=3, legend_at_bottom=True)
gauge_chart.title = 'XYZ'
gauge_chart.range = [0, 1000]

for i, skill in enumerate(list):
	gauge_chart.add(skill, randomlist[i])



gauge_chart.render_to_file('newchart.svg')  

