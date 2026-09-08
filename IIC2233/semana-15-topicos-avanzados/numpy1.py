import numpy as np
import random as ran

matriz_1 = np.array([0, 1, 0])
matriz_2 = np.array([10, 10, 10])
matriz_mod = np.full((10, 10), ran.randint(0,2))

print(matriz_mod)

matriz_mod_2 = np.identity(5)
print(matriz_mod_2)