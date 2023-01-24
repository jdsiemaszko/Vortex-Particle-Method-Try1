"""
Full Simulation Run
"""
from processor import advection, calc_vel_field
from preprocessing import geometry_input, define_scene, initialise_scene
from const import *

geo, u, l = geometry_input(file)
scn = define_scene(u, l)
initialise_scene(scn)

for i in range(int(10)):
    # plot_scene(geo, u, l, scn)
    # plot_particle_vel(geo, u, l, scn)
    pos, vel = calc_vel_field(scn, u, l)
    plot_vel_field(pos, vel, geo, u, l)
    scn = advection(scn)
    print('advection step finished')
