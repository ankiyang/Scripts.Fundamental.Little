import pygal

from math import cos

xy_chart = pygal.XY()
xy_chart.title('XY cosinus')
# xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
# xy_chart.add('x = 1',  [(1, -5), (1, 5)])
# xy_chart.add('x = -1', [(-1, -5), (-1, 5)])
xy_chart.add('y = 1',  [(-5, 1), (5, 1)])
xy_chart.add('y = -1', [(-5, -1), (5, -1)])
xy_chart.render_to_file('xy_chart.svg')