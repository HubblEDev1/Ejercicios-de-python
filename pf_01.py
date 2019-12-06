# -*- coding: utf-8 -*-
"""
1. Given a file with results from matches between soccer teams, write a Python program
to generate a table with team positions. In the input file, each row must contain three
columns separated by a ‘;’ indicating the two team names and the result of the match
for the first team. For example ‘America;Chivas;Win’, means that ‘America’ won the
match against ‘Chivas’; whilst ‘Santos;Atlas;Loose’ means that ‘Santos’ lost the match
against ‘Atlas’. A victory equals 3 points, and a draw equals 1 point. The output must
include the position, the team name, the number of matches played (MP), the number
of victories (W), the number of draws (D), the number of losses (L) and the total points.

"""

wd = '/Users/edsol/Documents/proyecto_final/'
file = wd + 'partidos.txt'

d = {}
l = []

with open(file, 'r', encoding = 'utf-8') as f:
    aux = []
    for line in f:
        aux = line.strip().split(';');
        if aux[0] not in d:
            d[aux[0]] = [0,0,0,0,0]
        if aux[1] not in d:
            d[aux[1]] = [0,0,0,0,0]
            
        d[aux[0]][0] += 1   #agrega partido jugado a los dos equipos
        d[aux[1]][0] += 1   
        if aux[2] == 'Win':
            d[aux[0]][1] += 1   #agrega victoria
            d[aux[0]][4] += 3   #agrega puntos al ganador
            d[aux[1]][3] += 1   #agrega derrota
        else:
            d[aux[0]][2] += 1  #agrega empate
            d[aux[1]][2] += 1
            d[aux[0]][4] += 1   #agrega un punto a cada uno
            d[aux[1]][4] += 1
            
#for k,v in d.items():
n = len(d)
count = 1
k = ''

while n > 0:
    i = 0
    for k,v in d.items():
        if i == 0:
            maximo = k
        if v[4] > d[maximo][4]:
            maximo = k
        i += 1
    print(count,maximo,d[maximo])
    d.pop(maximo)
    n -= 1
    count += 1
    
#print(d)
            