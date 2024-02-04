import numpy as np
import numpy.linalg as la


A = np.array([[4, 2, -2],
              [2, 1, -1],
              [3, 1, -2]])

print(la.det(A))