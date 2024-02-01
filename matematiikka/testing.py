import numpy as np


def eliminate(system):
    system_length = len(system)
    for i in range(1, system_length):
        if system[i][0] != 0:
            x = -system[i][0]/system[i-1][0]
            system[i][0] += x
    return

system = np.array([[2, 1, 1, 6], [1, 3, 1, 2], [2, 1, 2, 9]])
eliminate(system)
print(system)