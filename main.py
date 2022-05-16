import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':


    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #theta = np.linspace(-50000 * np.pi, 50000 * np.pi, 9)
    z = [1,2,3,4,5,6,7,8,9,10,11,12]
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [1,2,3,4,5,6,7,8,9,10,11,12]
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()

    plt.show()