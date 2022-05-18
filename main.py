import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def get_V(a,b): #a - вектор Солнца, b - вектор астероида
    G = 132712440043.85333# km^3/sec^2 - гравитационная постоянная Солнца.
    m = 1,989E+30# кг - масса Солнца
    Gm = (G*m)**(1/2)
    new_vector = [0]*4

    new_vector[0] = a[0]
    for i in range(1,4):
        new_vector = Gm*(((a[1]-b[1])/(a[1]-b[1])**2)**1/2)

def Gaus(asteroid_matrix, Sun_matrix):
    pass


if __name__ == '__main__':

    x0 = 9.024986646096280E+07
    y0 = -1.796241168371621E+08
    z0 = 2.872704561684193E+07

    V_x0 = 1.221265881140648E+01
    V_y0 = 2.336492505157211E+01
    V_z0 = -3.695786432289606E+00



    print(x0 + y0)

    """mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #theta = np.linspace(-50000 * np.pi, 50000 * np.pi, 9)
    z = [1,2,3,4,5,6,7,8,9,10,11,12]
    x = [1,2,3,4,5,6,7,8,9,10,11,12]
    y = [1,2,3,4,5,6,7,8,9,10,11,12]
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()"""

    plt.show()