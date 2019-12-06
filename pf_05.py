# -*- coding: utf-8 -*-

import numpy as np
import random as rm

figure = np.arange(1,17)

res = np.copy(figure)
rm.shuffle(figure)
figure = figure.reshape(4,4)

#print(figure)
#print(res)

#if figure.all() == res.all():
#    print('si')
#else :
#    print('no')


#captura las posiciones del cero incial
a = -1
for i in range(4):
    for j in range(4):
        if figure[i][j] == 16:
            a = i
            b = j
            break
    if a != -1:
        break

def print_fig():
    print('Welcome! Here is your puzzle:')
    for i in range(4):
        print('|-------------------------------|')
        s = '|   '
        for j in range(4):
            if figure[i][j] == 16:
                s += '\t|   '
            else:
                s += str(figure[i][j])+'\t|   '
        print(s)
    print('|-------------------------------|')



def evalua(n):
    aux = [1,1,1,1]
    if a == 0:
        aux[0] = 0
    elif a == 3:
        aux[1] = 0
    if b == 0:
        aux[2] = 0
    elif b == 3:
        aux[3] = 0
    
    if aux [0] and figure[a-1][b] == n:
        figure[a][b] = n
        figure[a-1][b] = 16
#        a = a-1
        return 0
    elif aux [1] and figure[a+1][b] == n:
        figure[a][b] = n
        figure[a+1][b] = 16
#        a = a+1
        return 1
    elif aux [2] and figure[a][b-1] == n:
        figure[a][b] = n
        figure[a][b-1] = 16
#        b = b-1
        return 2
    elif aux [3] and figure[a][b+1] == n:
        figure[a][b] = n
        figure[a][b+1] = 16
#        b = b+1
        return 3
    else:
        return 4
    
def comprobacion():
    for i,v in enumerate(figure.reshape(16)):
        if v != res[i]:
            return 1
    return 0
#print(i)
    


print_fig()
n=1
while n != 0 and comprobacion():
    n = int(input('Enter a number to move: '))
    opc = evalua(n)
    if opc < 4:
        print_fig()
#        print("(",a,b,")")
        if opc == 0:
            a = a-1
        elif opc == 1:
            a = a+1
        elif opc == 2: 
            b = b-1
        elif opc == 3:
            b = b+1
    elif n == 0:
        break
    else:
        print("Tile", n, "cannot be moved! Try another one.")
else:
    print("Juego terminado")
#print(figure[a][b])



