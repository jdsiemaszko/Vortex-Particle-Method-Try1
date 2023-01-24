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
    # if norm < radius:
    return rot90(vec) / kconst * (norm**4 + 3 * (radius * norm) **2 + 4 * radius**4)/(radius**2+norm**2)**3
    # else:
    #     return 0.



def advection(scene, timestep:float = dt):
    """
    Advection operation for the flow field:
    vortex particles are repositioned
    :param VP_field:
    :return: field with adjusted particle positions
    """

    for particle in scene:
        # vel = np.array([0., 0.])
        vel = vinf.copy()
        for particle2 in scene:
            dist = np.linalg.norm(particle2.pos - particle.pos)
            if dist != 0:
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

def calc_vel_field(scene, upperfunc, lowerfunc, bounds:tuple = domain, grid_size:float = h):
    xl, xu, yl, yu = bounds

    right = np.array([grid_size, 0])
    up = np.array([0, grid_size])
    p0 = np.array([xl + grid_size / 2, yl + grid_size / 2])

    irange = int((xu - xl) / grid_size)
    jrange = int((yu - yl) / grid_size)

    poslist = [0.] * (irange*jrange)
    vellist = [0.] * (irange * jrange)
    for i in range(irange):
        for j in range(jrange):
            index = i * jrange + j
            p = p0 + i * right + j * up
            velp = np.array([0., 0.])
            if not (0. <= p[0] <= 1.) or not (lowerfunc(p[0]) <= p[1] <= upperfunc(p[0])):
                velp = vinf.copy()
                for particle in scene:
                    dist = np.linalg.norm(particle.pos - p)
                    if dist != 0:
                        velp += K_epsilon(p, particle.pos) * particle.vort  # sign may be wrong

            poslist[index] = p
            vellist[index] = velp
    return np.array(poslist), np.array(vellist)