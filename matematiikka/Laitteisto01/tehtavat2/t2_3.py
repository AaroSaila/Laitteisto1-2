import numpy as np

u = np.array([2, 3])

v = np.array([4, -7])

uu = np.array([1, 1, 1])

vv = np.array([3, -3, 2])

vectors = [u, v, uu, vv]

for vector in vectors:
    norm = np.linalg.norm(vector)
    print(norm)
