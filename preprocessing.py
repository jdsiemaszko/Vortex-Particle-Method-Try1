"""
Import Airfoil Geometry
"""
import numpy as np
import scipy.interpolate
import pandas as pd
import matplotlib.pyplot as plt
from const import *
import random

def geometry_input(filename:str):
    """
    :param filename:
    :return:
    Airfoil Geometry in filename
    """
    with open(filename, 'r') as f:
        data = f.readlines()

        points = []

        # Data cleanup
        for row in data:
            row_split = row.split()
            try:
                points.append([float(row_split[0]), float(row_split[1])])
            except:
                # print('not a float')
                pass
        splitting_index = 0
        for i in range(len(points) - 1):
            if points[i + 1] < points[i]:
                splitting_index += 1

        # doesn't matter if those are switched btw
        upper_edge = np.array(points[:splitting_index])
        lower_edge = np.array(points[splitting_index:])
        points = np.array(points)

        upper_edge_func = scipy.interpolate.interp1d(upper_edge[:, 0], upper_edge[:, 1], kind='cubic', fill_value='extrapolate')
        lower_edge_func = scipy.interpolate.interp1d(lower_edge[:, 0], lower_edge[:, 1], kind='cubic', fill_value='extrapolate')
    return points, upper_edge_func, lower_edge_func

    # return pd.read_csv(filename, sep=" ", header=None)[1:].to_numpy()
    # return np.genfromtxt(filename, delimiter=",", skip_header=True, dtype=float)

def define_scene(upperfunc, lowerfunc, bounds:tuple = domain, grid_size:float = h):
    """
    define the initial grid of particles
    :param upperfunc:
    :param lowerfunc:
    :param bounds:
    :param grid_size:
    :return: list of particles, with initial positions
    """
    xl, xu, yl, yu = bounds

    right = np.array([grid_size, 0])
    up = np.array([0, grid_size])
    p0 = np.array([xl + grid_size/2, yl + grid_size/2])

    irange = int((xu - xl)/grid_size)
    jrange = int((yu-yl)/grid_size)
    scene = [0.]*(irange*jrange)

    for i in range(irange):
        for j in range(jrange):
            p = p0 + i * right + j * up
            if not(0. <= p[0] <= 1.) or not(lowerfunc(p[0]) <= p[1] <= upperfunc(p[0])):
                """
                note: this sucks
                """
                index = i*jrange + j
                scene[index] = Particle(pos=p, vel = [0., 0.], vort = 0., vol = 1.)
    print('initial positions defined')
    return list(filter(lambda a: a != 0., scene))

def initialise_scene(scene):
    for particle in scene:
        # particle.vort = (random.random()-0.5)
        particle.vort = particle.pos[0]/100
        # print(particle.vort)



if __name__ == '__main__':
    geo, u, l = geometry_input(file)
    scn = define_scene(u, l)
    ylist = np.linspace(0., 1., 101)
    plt.plot(geo[:,0], geo[:,1], 'r--', label=file)
    # plt.plot(ylist, np.vectorize(u)(ylist), 'r--', label="upper edge")
    # plt.plot(ylist, np.vectorize(l)(ylist), 'b--', label="lower edge")

    partxlist = []
    partylist = []
    for particle in scn:
        try:
            partxlist.append(particle.pos[0])
            partylist.append(particle.pos[1])
        except:
            pass
    plt.scatter(partxlist, partylist, label='particle positions')

    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()