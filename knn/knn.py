
import math
import numpy as np
import collections
import random as rd

def euklides(lista1, lista2):
    wynik = 0
    for i in range (len(lista1)-1):
        wynik+=(lista1[i]- lista2[i])**2
    return math.sqrt(wynik)

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
              tmp = euklides(line, tmp, True)
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
x = []

with open('datasets/australian.dat', 'r') as file:
    for line in file:
        tmp = line.split()
        tmp = list(map(lambda e: float(e), tmp))
        x.append(tmp)

print('Podaj który wiersz datasetu ma być porównywany ( max', len(x), '):')
l = int(input())
print('Podaj wartość parametru k:')
k = int(input())

listaklas = dystanse(x[l], x)

listaklas = sorted(listaklas)

slownik = doslownika(listaklas)

h = dystanseslownik(slownik)

slownik1 = slownik[1]
slownik0 = slownik[0]

for klasa in range(len(slownik)):
dystans1suma = sum(slownik1[:k])
dystans0suma = sum(slownik0[:k])
dystans0 = [0, dystans0suma]
dystans1 = [1, dystans1suma]
if dystans0[1] > dystans1[1]:
    print('Klasa decyzyjna to 0')
else:
    print('Klasa decyzyjna to 1')
