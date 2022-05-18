import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
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

def read(path):
    f = open(path) # Заменить на нужное имя файла. Файл подаётся без шапки и конца.
    # Только со значениями. Пример в репозитории
    l = [line.strip() for line in f]
    array = [] # Список списков.
    # Каждый элемент array - список значений [X,Y,Z]
    for i in range(1, len(l), 4):
        s = [float(s) for s in re.findall(r'-?\d+\.?\d*', l[i])]
        s[0] = s[0]*(10**(s[1]))
        del s[1]
        s[1] = s[1] * (10 ** s[2])
        del s[2]
        s[2] = s[2] * (10 ** s[3])
        del s[3]
        array.append(s)
    return array

if __name__ == '__main__':

    x0 = 9.024986646096280E+07
    y0 = -1.796241168371621E+08
    z0 = 2.872704561684193E+07

    V_x0 = 1.221265881140648E+01
    V_y0 = 2.336492505157211E+01
    V_z0 = -3.695786432289606E+00



    print(x0 + y0)

    vector_X = []
    vector_Y = []
    vector_Z = []
    coords = read('./Считывание/demo.txt')
    print(coords)

    for coord in coords:
        vector_X.append(coord[0])
        vector_Y.append(coord[1])
        vector_Z.append(coord[2])
    print(vector_X)
    print(vector_Y)
    print(vector_Z)

    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-50000 * np.pi, 50000 * np.pi, 10000000)
    ax.plot(vector_X, vector_Y, vector_Z, label='Орбита астероида 9162 Kwiila (1987 OA)')
    ax.legend()
    
    plt.show()