import math
import numpy as np
import collections
import random as rd
x = []

def euklides(lista1, lista2):
    wynik = 0
    for i in range (len(lista1)-1):
        wynik+=(lista1[i]- lista2[i])**2
    return math.sqrt(wynik)

def euklides2(lista1, lista2, utnij = False):
    if utnij:
        lista1 = lista1[:-1]
        lista2 = lista2[:-1]
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    c = v1-v2
    c = np.dot(c, c)
    return math.sqrt(c)

def dystanse(line, file):
    dyst = []
    i = 0
    for linia in file:
       if i < len(file)-1:
           tmp = file[i]
           if tmp == line:
               i += 1
           else:
              klasa = int(tmp[-1])
              tmp = euklides2(line, tmp, True)
              dystanseup = [klasa, tmp]
              dyst.append(dystanseup)
              i += 1
    return dyst


def doslownika(list):
    i = 0
    slownik = {}
    for line in list:
        if i < len(list)-1:
            tmp = list[i]
            klasa = tmp[0]
            odleglosc = tmp[1]
            if klasa in slownik:
                slownik[klasa].append(odleglosc)
            else:
                slownik[klasa] = []
                slownik[klasa].append(odleglosc)
            i += 1
    return slownik

def dystanseslownik(slownik):
    s = {}
    for i in range(len(slownik)):
        s["{0}".format(i)] = sum(slownik[i])
    return s


'''Metoda całkowania Monte-carlo'''

def monte_carlo(function, a, b, punkty):
    maxValue = max(map(lambda i: function(i), np.linspace(a, b, punkty, True)))
    points = [(rd.uniform(a, b), rd.uniform(0, maxValue)) for x in range(punkty)]

    lower = upper = 0
    for x in points:
        if x[1] < function(x[0]):
            lower += 1
        else:
            upper += 1

    return maxValue(b - a)(lower / (lower + upper))


def riemann(function, a, b, precision):
    points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    diff = (b - a) / (precision - 1)

    area = 0
    for x in points[1:]:
        area += diffx

    return area


def trapmann(function, a, b, precision):
    points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
    diff = (b - a) / (precision - 1)

    area = 0
    for x in range(1, precision):
        area += diff(points[x] + points[x - 1]) / 2

    return area

def srednia(lista):
    suma = 0.0
    for wartosc in lista:
        suma += wartosc
    s = float(suma/(float(len(lista))))
    return s

def wariancja(lista):
    s = srednia(lista)
    suma = 0.0
    for wartosc in lista:
        suma += (wartosc - s)^2
    w = float(suma/(float(len(lista))))
    return w

def odchylenie_standardowe(lista):
    odchylenie = math.sqrt(wariancja(lista))
    return odchylenie





with open('datasets/australian.dat', 'r') as file:
    for line in file:
        tmp = line.split()
        tmp = list(map(lambda e: float(e), tmp))
        x.append(tmp)

macierz = [(2,1), (5,2), (7,3), (8,3)]

macierz1 = np.ones((4,2))

print(macierz1)
