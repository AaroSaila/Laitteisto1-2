import numpy as np
import numpy.linalg as la


def solve_system(system):
    A = system[0]
    B = system[1]
    determinant = la.det(A)
    if determinant == 0.0:
        least_squares = la.lstsq(A, B, rcond=None)
        X = []
        X.append(round(least_squares[0][0][0], 0))
        X.append(round(least_squares[0][1][0], 0)) 
        X.append(round(least_squares[0][2][0], 0))
        result = np.array([[A[0][0] * X[0] + A[0][1] * X[1] + A[0][2] * X[2]], 
                           [A[1][0] * X[0] + A[1][1] * X[1] + A[1][2] * X[2]],
                           [A[2][0] * X[0] + A[2][1] * X[1] + A[2][2] * X[2]]])
        if np.array_equal(result, B):
            print("System has an infinite amount of solutions")
        else:
            print("System has no solutions")

    else:
        X = la.inv(A).dot(B)
        print(f"x = {X[0]}")
        print(f"y = {X[1]}")
        if len(X) == 3:
            print(f"z = {X[2]}")
        print("\n")


# a)

print("a)")
solve_system((
    np.array([[5, 3],
              [2, 1]]),
    np.array([[9],
              [4]])
))

# b)

print("b)")
solve_system((
    np.array([[2, 1, 1],
              [1, 3, 1],
              [2, 1, 2]]),
    np.array([[6],
              [2],
              [9]])
))

# c)

print("c)")
solve_system((
    np.array([[1, 1, 3],
              [3, 1, 1],
              [2, 1, 2]]),
    np.array([[-1],
              [5],
              [2]])
))
