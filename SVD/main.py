
import math
import numpy as np
import collections
import random as rd

def macierz_u(macierz):
    wiersz1 = macierz[0]
    wiersz2 = macierz[1]
    wartosci = np.linalg.eigh(macierz)
    wartosci = wartosci[0]
    lambdy1 = []
    lambdy1.append([wartosci[0], 0])
    lambdy1.append([0, wartosci[0]])
    lambdy2 = []
    lambdy2.append([wartosci[1], 0])
    lambdy2.append([0, wartosci[1]])
    return lambdy1
    








A = np.array([[1, 2, 0], [2, 1, 0]])

AAT = np.dot(A, A.T)
ATA = np.dot(A.T, A)

w = macierz_u(AAT)
print(w)
