"""
Flow condition processor
"""
from const import *
from geometry_input import geometry_input

# vortex particle needs: velocity components, vorticity value, volume?
class Particle:
    def __init__(self, pos, vort:float, vol:float):
        self.pos = pos
        self.vort = vort
        self.vol = vol




def advection(VP_field):
    """
    Advection operation for the flow field:
    vortex particles are repositioned
    :param VP_field:
    :return: field with adjusted particle positions
    """
    for particle in VP_field:


def diffusion(VP_field):
    """
    Diffusion operation for the flow field
    :param VP_field:
    :return: field with adjusted vorticity values
    """

    for particle in VP_field:




