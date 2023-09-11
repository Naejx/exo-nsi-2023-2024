# Créé par j.guerin1, le 11/09/2023 en Python 3.7
from collections import deque

f = []
f = deque()

def enfile(f, nbr):
    """enfile(f, X)<- remplacer X par un nombre,
    pour en mettre plusieurs enfile(f, (X, X1, ...)"""
    if type(nbr) != int:
        for i in range(len(nbr)):
            f.appendleft(nbr[i])
    else:
        f.appendleft(nbr)
    return list(f)



