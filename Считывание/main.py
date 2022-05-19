import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
import matplotlib.pyplot as plt


def get_V(a, b):  # a - вектор Солнца, b - вектор астероида
    G = 132712440043.85333  # km^3/sec^2 - гравитационная постоянная Солнца.
    m = 1, 989E+30  # кг - масса Солнца
    Gm = (G * m) ** (1 / 2)
    new_vector = [0] * 4

    new_vector[0] = a[0]
    for i in range(1, 4):
        new_vector = Gm * (((a[1] - b[1]) / (a[1] - b[1]) ** 2) ** 1 / 2)


def Gaus(asteroid_matrix, Sun_matrix):
    pass


def read(path):
    f = open(path)  # Заменить на нужное имя файла. Файл подаётся без шапки и конца.
    # Только со значениями. Пример в репозитории
    l = [line.strip() for line in f]
    array = []  # Список списков.
    # Каждый элемент array - список значений [X,Y,Z]
    for index in range(1, len(l), 4):
        coordinates = [float(coordinates) for coordinates in re.findall(r'-?\d+\.?\d*', l[index])]
        coordinates[0] = coordinates[0] * (10 ** (coordinates[1]))
        del coordinates[1]
        coordinates[1] = coordinates[1] * (10 ** coordinates[2])
        del coordinates[2]
        coordinates[2] = coordinates[2] * (10 ** coordinates[3])
        del coordinates[3]
        velocity = [float(velocity) for velocity in re.findall(r'-?\d+\.?\d*', l[index+1])]
        velocity[0] = velocity[0] * (10 ** (velocity[1]))
        del velocity[1]
        velocity[1] = velocity[1] * (10 ** velocity[2])
        del velocity[2]
        velocity[2] = velocity[2] * (10 ** velocity[3])
        del velocity[3]
        coordinates.append(velocity[0])
        coordinates.append(velocity[1])
        coordinates.append(velocity[2])
        array.append(coordinates)
    return array


if __name__ == '__main__':

    vector2_X = []
    vector2_Y = []
    vector2_Z = []
    velocity2_X = []
    velocity2_Y = []
    velocity2_Z = []
    coords2 = read('./Считывание/demo2.txt')
    print(coords2)

    for coord in coords2:
        vector2_X.append(coord[0])
        vector2_Y.append(coord[1])
        vector2_Z.append(coord[2])
        velocity2_X.append(coord[3])
        velocity2_Y.append(coord[4])
        velocity2_Z.append(coord[5])
    print(vector2_X)
    print(vector2_Y)
    print(vector2_Z)

    vector_X = []
    vector_Y = []
    vector_Z = []
    velocity_X = []
    velocity_Y = []
    velocity_Z = []
    coords = read('./Считывание/demo.txt')
    print(coords)

    for coord in coords:
        vector_X.append(coord[0])
        vector_Y.append(coord[1])
        vector_Z.append(coord[2])
        velocity_X.append(coord[3])
        velocity_Y.append(coord[4])
        velocity_Z.append(coord[5])
    print(vector_X)
    print(vector_Y)
    print(vector_Z)

    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-50000 * np.pi, 50000 * np.pi, 10000000)
    ax.plot(vector2_X, vector2_Y, vector2_Z, label='Орбита астероида 2340 Hathor (1976 UA)', color=(0.9, 0.2, 0.9))
    ax.plot(vector_X, vector_Y, vector_Z, label='Орбита астероида 9162 Kwiila (1987 OA)')
    ax.legend()

    plt.show()