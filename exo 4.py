# Créé par j.guerin1, le 11/09/2023 en Python 3.7
from collections import deque

E ='(2+3)*4-(2+8)'

def separeE(E):
    nombres = []
    operations = []
    for i in range(len(E)):
        if E[i].isdigit():
            nombres.append(E[i])
        else:
            operations.append(E[i])

    return nombres, operations

def controle(N, O):
    result = None
    A = 0
    B = 0
    for i in range(len(O)):
        if O[i] == '(':
            A += 1
        if O[i] == ')':
            B += 1
    if A == B:
        result = True
    else:
        result = False
    return result


print(controle(separeE(E)[0], separeE(E)[1]))

