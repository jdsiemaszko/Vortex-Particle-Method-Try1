"""
Flow condition processor
"""


# vortex particle needs: velocity components, vorticity value, volume?
class Particle:
    def __init__(self, pos, vort:float, vol:float):
        self.pos = pos
        self.vort = vort
        self.vol = vol




def advection(VP_field):
    for particle in VP_field:


def diffusion(VP_field):



