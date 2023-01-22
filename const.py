"""
Constants and universal functions definitions
"""


dt = 1e-3
h = 5e-2
# computation bounds
xl = -1.
xu = 2.

yl = -1
yu = 1
domain = (xl, xu, yl, yu)


file = 'E546.dat'

# vortex particle needs: velocity components, vorticity value, volume?
class Particle:
    def __init__(self, pos,vel, vort:float, vol:float):
        self.pos = pos
        self.vel = vel
        self.vort = vort
        self.vol = vol
