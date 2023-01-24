"""
Constants and universal functions definitions
"""
import numpy as np
import matplotlib.pyplot as plt
dt = 1e-2
h = 1e-1
epsilon = 3*h

vinf = np.array([10., 0.])
# computation bounds
xl = -1.
xu = 2.

yl = -1
yu = 1
domain = (xl, xu, yl, yu)


file = 'E546.dat'
plot_size = 5.

# vortex particle needs: velocity components, vorticity value, volume?
class Particle:
    def __init__(self, pos,vel, vort:float, vol:float):
        self.pos = pos
        self.vel = vel
        self.vort = vort
        self.vol = vol

def plot_scene(geo, u, l, scene):
    """
    Plot the scene
    :param geo: geometry
    :param scene: particles
    :return: graphs baby
    """
    ylist = np.linspace(0., 1., 101)
    # plt.plot(geo[:, 0], geo[:, 1], 'r', label=file)
    # plt.plot(ylist, np.vectorize(u)(ylist), 'r--', label="upper edge")
    # plt.plot(ylist, np.vectorize(l)(ylist), 'b--', label="lower edge")
    plt.fill_between(ylist, np.vectorize(u)(ylist), np.vectorize(l)(ylist))

    partxlist = []
    partylist = []
    for particle in scene:
        try:
            partxlist.append(particle.pos[0])
            partylist.append(particle.pos[1])
        except:
            pass
    plt.scatter(partxlist, partylist, label='particle positions', s=[plot_size]*len(partxlist))

    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def plot_particle_vel(geo, u, l, scene):
    ylist = np.linspace(0., 1., 101)
    plt.fill_between(ylist, np.vectorize(u)(ylist), np.vectorize(l)(ylist), label=file)


    poslist = []
    vellist = []
    for particle in scene:
        try:
            poslist.append(particle.pos)
            vellist.append(particle.vel)
        except:
            pass

    poslist = np.array(poslist)
    vellist = np.array(vellist)

    plt.scatter(poslist[:, 0], poslist[:, 1], color='black', s = [plot_size]*len(poslist))
    plt.quiver(poslist[:, 0], poslist[:, 1], vellist[:, 0], vellist[:, 1], color ='red', label="particle velocity")

    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()

def plot_vel_field(poslist, vellist, geo, u, l):
    ylist = np.linspace(0., 1., 101)
    plt.fill_between(ylist, np.vectorize(u)(ylist), np.vectorize(l)(ylist), label=file)
    # plt.scatter(poslist[:, 0], poslist[:, 1], color='black', s=[plot_size] * len(poslist))
    plt.quiver(poslist[:, 0], poslist[:, 1], vellist[:, 0], vellist[:, 1], color='red', label="velocity")
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()
