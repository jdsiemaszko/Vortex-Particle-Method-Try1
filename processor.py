"""
Flow condition processor:
advection step
diffusion step
remember to store scenes at each timestep!
"""
from const import *
import numpy as np
from preprocessing import geometry_input, define_scene
import math

kconst = 1 / 2 / math.pi
def K_function(pos1, pos2):
    norm = np.linalg.norm(pos1 - pos2)
    return (pos1-pos2) * kconst / norm**2

def gauss_mollifier(pos1, pos2):
    norm = np.linalg.norm(pos1 - pos2)
    if norm < 1:
        return math.exp(-1/(1-norm**2))
    else:
        return 0.

def gauss_mollifier_norm(norm):
    if norm < 1:
        return math.exp(-1 / (1 - norm ** 2))
    else:
        return 0.

def mollifier_epsilon(norm, radius:float = epsilon):
    return gauss_mollifier_norm(norm/radius) / radius**2


def rot90(vec):
    matrix = np.array([[0, -1], [1, 0]])
    return np.matmul(matrix, vec)

def K_epsilon(pos1, pos2, radius:float = epsilon):
    vec = pos1 - pos2
    norm = np.linalg.norm(vec)
    return rot90(vec) / kconst * (norm**4 + 3 * (radius * norm) **2 + 4 * radius**4)/(radius**2+norm**2)**3



def advection(scene, timestep:float = dt):
    """
    Advection operation for the flow field:
    vortex particles are repositioned
    :param VP_field:
    :return: field with adjusted particle positions
    """

    for particle in scene:
        omega = particle.vort
        vel = np.array([0., 0.])
        for particle2 in scene:
            dist = np.linalg.norm(particle2.pos - particle.pos)
            if dist != 0:
                omega += mollifier_epsilon(dist)
                vel += K_epsilon(particle.pos, particle2.pos) * particle2.vort  # sign may be wrong

        particle.pos += vel * timestep
        particle.vel = vel
    return scene


# def diffusion(scene):
#     """
#     Diffusion operation for the flow field
#     :param VP_field:
#     :return: field with adjusted vorticity values
#     """
#
#     for particle in scene:




