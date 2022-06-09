import math
import numpy as np
import collections
import random as rd


def dlugosc(u):
    '''return math.sqrt(sum(i**2 for i in u))'''
    return np.linalg.norm(u)


def projekcja(v1, v2):
    L = np.dot(v1.T, v2)
    M = np.dot(v1.T, v1)
    projekcja = (L/M)*v1
    return projekcja

def wartosc_e(u):
    e = u/dlugosc(u)
    return e

def macierz_Q(v1, v2):
    Q = np.array
    u1 = v1
    e1 = wartosc_e(u1)
    u2 = v2 - projekcja(v1, v2)
    e2 = wartosc_e(u2)
    Q = np.append([e1], [e2], axis=0)
    return Q.T

def macierz_R(A, macierzQ):
    R = np.dot(macierzQ.T, A)
    return R


A = np.array([[1, 0],
             [1, 1],
             [0, 1]])

v1 = A.T[0]
v2 = A.T[1]

Q = macierz_Q(v1, v2)
R = macierz_R(A, Q)

'''macierz Q'''
print(Q)
'''Macierz R'''
print(R)
'''Sprawdzenie'''
print(np.dot(Q, R))


'''Wynik z konsoli
Q = [[ 0.70710678 -0.40824829]
     [ 0.70710678  0.40824829]
     [ 0.          0.81649658]]
     
R = [[1.41421356 0.70710678]
     [0.         1.22474487]]

Q*R = [[ 1.00000000e+00 -2.26449897e-16]
       [ 1.00000000e+00  1.00000000e+00]
       [ 0.00000000e+00  1.00000000e+00]]

'''
