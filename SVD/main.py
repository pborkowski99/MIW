import math
import numpy as np
import collections
import random as rd

def macierz_u(AAT):
    wiersz1 = AAT[0]
    wiersz2 = AAT[1]
    wartosci = np.linalg.eigh(AAT)
    wartosci = wartosci[1]

    return wartosci

def macierz_sigma(AAT):
    wartosci = np.linalg.eigh(AAT)
    wartosci = wartosci[0]
    sigma = []
    sigma.append([wartosci[0], 0, 0])
    sigma.append([0, wartosci[1], 0])
    return sigma

def macierz_v(ATA):
    wartosci = np.linalg.eigh(ATA)
    wartosci = wartosci[1]
    return wartosci





A = np.array([[1, -2, 0], [0, -2, 1]])

AAT = np.dot(A, A.T)
ATA = np.dot(A.T, A)

U = macierz_u(AAT)
V = macierz_v(ATA)
V= V.T
Sigma = macierz_sigma(AAT)
print(U)
print(Sigma)
print(V)
'''Wynik z konsoli
U =[[-0.70710678  0.70710678]
    [ 0.70710678  0.70710678]]
Sigma = [[1.0, 0, 0], 
         [0, 9.0, 0]]
V = [[-6.66666667e-01 -3.33333333e-01 -6.66666667e-01]
     [-7.07106781e-01 -1.88247990e-16  7.07106781e-01]
     [ 2.35702260e-01 -9.42809042e-01  2.35702260e-01]]'''
