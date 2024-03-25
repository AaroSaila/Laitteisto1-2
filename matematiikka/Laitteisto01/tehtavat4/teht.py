import sympy as sp
from sympy.abc import x, y, z


print("osa 2\n")

print("1.\n")

print("a)\n")
print(sp.solve([x - 2*y - 2*z, 
                -2*x + y - z + 3,
                3*x + 2*y + z - 4], [x, y, z]), "\n")

print("b)\n")
print(sp.solve([x + y - 1,
                2*x + y - z - 1,
                3*x + y - 2*z - 1]), "\n")

print("2.\n")

print("a)\n")
print(sp.solve([2*x + 4*y - z - 11,
                6*x - y - 3*z - 7,
                4*x + 5*y - 2*z - 16]), "\n")

print("b)\n")
print(sp.solve([4*x + 2*y - 2*z,
                2*x + y - z - 1,
                3*x + y - 2*z - 1]), "\n")

print("osa 3\n")

print("1\n")

print("a)\n")
print(sp.solve([5*x + 3*y - 9,
                2*x + y - 4]), "\n")

print("b)\n")
print(sp.solve([2*x + y + z - 6,
                x + 3*y + z - 2,
                2*x + y + 2*z - 9]), "\n")

print("c)\n")
print(sp.solve([x + y + 3*z + 1,
                3*x + y + z - 5,
                2*x + y + 2*z -2]), "\n")
