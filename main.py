"""
Full Simulation Run
"""
from processor import advection
from preprocessing import geometry_input, define_scene
from const import *

geo, u, l = geometry_input(file)
scn = define_scene(u, l)

for i in range(int(10)):
    plot_scene(geo, u, l, scn)
    scn = advection(scn)
    print('advection step finished')
