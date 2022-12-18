import pygal
import random
from pygal.style import Style


list = ['Skill1', 'Skill2', 'Skill3', 'Skill4']

randomlist = []
#test = []
for _ in range(0,17):
	n = random.randint(1, 100)
	randomlist.append(n)
	

gauge = pygal.SolidGauge(inner_radius=0.70, width=1920, height=1080 ,legend_at_bottom=True)
percent_formatter = lambda x: '{:.10g}%'.format(x)
gauge.value_formatter = percent_formatter
gauge.title = 'XYZ'


for i, skill in enumerate(list):
    gauge.add(skill, [{'value': randomlist[i], 'max_value': 100}])



gauge.render_to_file('newchart.svg')  
