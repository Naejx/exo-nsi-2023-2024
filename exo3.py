# Créé par j.guerin1, le 07/09/2023 en Python 3.7
E = '3+5*7-2'

def separeE(E):
    nombres = []
    operations = []
    for i in range(len(E)):
        if E[i].isdigit():
            nombres.append(E[i])
        else:
            operations.append(E[i])

    return nombres, operations

print(separeE(E))
