# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 20:37:14 2019

@author: HiramGC

4. In the popular game Minesweeper (Buscaminas) there is a board where some cells
contain mines, and every cell without a mine contains an integer indicating the total
number of mines surrounding such cell. Given a positive integer n, write a Python
program that generates a nxn array that contains floor(nxn/2) mines in random cells,
with a 1 where there is a mine, and a 0 where there is not. Afterwards, the program
must generate a valid configuration for the board. The configuration means to create a
nxn array with the number of mines that surrounds each cell. At the end, the program
must show the array with the positions of the mines and the configuration array.
"""

import random as rm
import numpy as np
import math as mt


n = 7

minas = mt.floor(n*n/2)

tablero = np.zeros(n*n)
rango = n*n-1
for m in range(minas):
    num = rm.randint(0,rango)
    while(tablero[num] == 1):
        num = rm.randint(0,rango)
    tablero[num] = 1

tablero = tablero.reshape(n,n)
print('posiciones = \n',tablero)


def adyacentes(i,j,aux):
    if aux [0][0]:
        if tablero[i-1][j-1] :
            config[i][j] += 1
    if aux [0][1]: 
        if tablero[i-1][j]:
            config[i][j] += 1
    if aux [0][2]:
        if tablero[i-1][j+1]:
            config[i][j] += 1
    if aux [1][0]:
        if tablero[i][j-1]:
            config[i][j] += 1
    if aux [1][2]:
        if tablero[i][j+1]:
            config[i][j] += 1
    if aux [2][0]:
        if tablero[i+1][j-1]:
            config[i][j] += 1
    if aux [2][1]:
        if tablero[i+1][j]:
            config[i][j] += 1
    if aux [2][2]:  
        if tablero[i+1][j+1]:
            config[i][j] += 1
            
config = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        aux = np.ones((3,3))
        if i == 0:
            aux[0][0] = 0
            aux[0][1] = 0
            aux[0][2] = 0
        if i == n-1:
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
        
print('configuracion = \n',config)