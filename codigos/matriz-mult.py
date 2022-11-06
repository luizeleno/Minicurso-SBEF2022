'''
Exemplos complicados do uso de zip(): matriz transposta e produto de matrizes, implementadas como listas.

Para comparação, mostro também o uso do numpy para o mesmo objetivo, o que requer a conversão das listas para arrays do numpy.
'''

A = [[1, 2], [3, 4]]
B = [[5, 6, 7], [8, 9, 10]]

# produto de matrizes
AB =  [[sum(a * b for a, b in zip (lA, cB)) for cB in zip(*B)] for lA in A]
print(AB)

# matriz transposta
AT = [[c for c in l] for l in zip(*A)]
print(AT)

# em numpy
import numpy as np
A, B = np.array(A), np.array(B)
AB = A @ B
print(AB)

AT = A.T
print(AT)
