"""
Import Airfoil Geometry
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from const import *
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
    return np.array(points)

    # return pd.read_csv(filename, sep=" ", header=None)[1:].to_numpy()
    # return np.genfromtxt(filename, delimiter=",", skip_header=True, dtype=float)

if __name__ == '__main__':
    geo = geometry_input(file)

    plt.plot(geo[:,0], geo[:,1], 'b--', label=file)
    plt.legend()
    plt.axis('equal')
    plt.grid()
    plt.show()