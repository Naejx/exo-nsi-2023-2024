# Créé par j.guerin1, le 11/09/2023 en Python 3.7

E = '[3 + (5 - 7) * 3]'

def separeE(E):
    nombres = []
    operations = []
    for i in range(len(E)):
        if E[i].isdigit():
            nombres.append(E[i])
        else:
            operations.append(E[i])

    return nombres, operations

def isitgood(N, O):
    result = False
    stack = []
    for i in range(len(O)):
        if O[i] == '(':
            stack.append('(')
        if O[i] == ')':
            if stack[-1] == '(':
                result = True
            stack.pop
        if O[i] == '[':
            stack.append('[')
        if O[i] == ']':
            if stack[-1] == '[':
                result = True
            stack.pop
    stack = []
    return result


print(isitgood(separeE(E)[0], separeE(E)[1]))


