# -*- coding: utf-8 -*-
"""
2. Write a Python program to play the “game of life”. The game consists in a bi-dimensional
mesh of cells. Each cell has two possible states: ‘live’ or ‘dead’. Each cell interacts with
all its neighbors and in each iteration of the game occurs the following transitions:
a. A cell dies if it has less than 2 living neighbors (because of subpopulation)
b. A cell dies if it has more than three living neighbors (because of overpopulation)
c. A cell survives to the next generation if it has two or three living neighbors.
d. A dead cell revives if it has exactly three living neighbors.
e. All transactions (deaths and rebirths) occur at the same time.
f. At the beginning of the game, all the cell states are initialized at random, and
then they are evolved ‘naturally’.
Show the state of mesh graphically using pyplot (use the function imshow).
"""

#import random as rm
import numpy as np
import matplotlib.pyplot as plt
#import os

m = 100
n = 100
gen = 100

#f = np.random.rand(10,10) #genera un arrglo de 5x3 con numeros aleatorios entre 0 y 1

pop = np.random.randint(0,2,(m,n)) #genera la poblacion inicial
pop = pop * 255



plt.imshow(pop)
#plt.colorbar()
plt.show()

mat = np.zeros((m,n,2))

def adyacentes(i,j,aux):
    if aux [0][0]:
        if pop[i-1][j-1] :
            mat[i][j][1] += 1
    if aux [0][1]: 
        if pop[i-1][j]:
            mat[i][j][1] += 1
    if aux [0][2]:
        if pop[i-1][j+1]:
            mat[i][j][1] += 1
    if aux [1][0]:
        if pop[i][j-1]:
            mat[i][j][1] += 1
    if aux [1][2]:
        if pop[i][j+1]:
            mat[i][j][1] += 1
    if aux [2][0]:
        if pop[i+1][j-1]:
            mat[i][j][1] += 1
    if aux [2][1]:
        if pop[i+1][j]:
            mat[i][j][1] += 1
    if aux [2][2]:  
        if pop[i+1][j+1]:
            mat[i][j][1] += 1





def evaluacion (i,j):
    if mat[i][j][0]:
        if mat[i][j][1] < 2:
            return 0
        elif mat[i][j][1] > 3:
            return 0
        else:
            return 255
    else:
        if mat[i][j][1] == 3:
            return 255
        else:
            return 0

pop2 = np.zeros((m,n))

while gen > 0:
    mat = np.zeros((m,n,2))
    for i in range(m):
        for j in range(n):
            mat[i][j][0] = pop[i][j]
            aux = np.ones((3,3))
            if i == 0:
                aux[0][0] = 0
                aux[0][1] = 0
                aux[0][2] = 0
            if i == m-1:
                aux[2][0] = 0
                aux[2][1] = 0
                aux[2][2] = 0
            if j == 0:
                aux[0][0] = 0
                aux[1][0] = 0
                aux[2][0] = 0
            if j == n-1:
                aux[0][2] = 0
                aux[1][2] = 0
                aux[2][2] = 0
            adyacentes(i,j,aux)
            pop2[i][j] = evaluacion(i,j)
    pop= np.copy(pop2)
#    os.system ("cls") 
#    os.system ("clear") 
#    clear()
#    clear_output()
    plt.imshow(pop)
    #plt.colorbar()
    plt.show()
    gen -=1


            
            
            
            
        
        
        