import numpy as np


print("Harjoitustehtavat 5.2.3\n")

a = np.array([[-1, 2],
              [3, 1]])
b = np.array([[0, 1, 3],
              [2, -3, 5]])
print("a) \n", np.matmul(a, b), "\n")

a = np.array([[1, 3, 5],
              [0, -2, 1],
              [2, -1, 4]])
b = np.array([[1],
             [-3],
             [-1]])
print("b) \n", np.matmul(a, b), "\n")

a = np.array([[2, 0, 1],
              [1, -3, 4],
              [0, 1, 5]])
b = np.array([[3],
              [-5],
              [7]])
print("c) \n", np.matmul(a, b), "\n")

a = np.array([[1, -4, 2],
              [3, 0, -2],
              [2, 1, 0]])
b = np.array([[5, 1, -1],
              [-2, 1, 3],
              [0, 3, 4]])
print("d) \n", np.matmul(a, b), "\n")


print("Transpoosit\n")

a = np.array([[4, 9, 0],
              [-3, 7, -11]])
b = np.array([[8, 9],
              [-3, 12],
              [0, -1],
              [7, 1]])
print(a.transpose(), "\n")
print(b.transpose(), "\n")


print("Harjoitustehtavat 5.4.1\n")

print("1.\n")

a = np.array([[5, -6],
              [8, 10]])
print("a)\n", np.linalg.det(a), "\n")


print("2.\n")

a = np.array([[2, 3, 4],
              [-2, -1, 1],
              [5, 3, 2]])
print("a)\n", np.linalg.det(a), "\n")

a = np.array([[3, 15, 7],
              [0, -4, 0],
              [3, 2, 3]])
print("b)\n", np.linalg.det(a), "\n")


print("Harjoitustehtavat 5.4.2\n")

a = np.array([[-2, 0, 8, 5],
              [3, -1, 2, 1],
              [4, 7, 6, 2],
              [1, 0, 2, 3]])
print(np.linalg.det(a))
