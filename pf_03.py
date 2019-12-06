# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 00:35:55 2019

@author: HiramGC

3. Given a text message containing only letters (lowercase) and spaces, write a Python
program to returns the minimum click distance to produce the message. To calculate
the distance, you can only move in the keyboard up, down, right and left (not in
diagonal), and cannot go directly to the space bar. Consider that the keyboard has a
QWERTY distribution, with the space bar located next to the letter ‘m’, as follows:
Keyboard = [‘qwertyuiop’,
 ‘asdfghjkl’,
 ‘zxcvbnm ‘]
"""
keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm ']

s = 'q e'
l = []
for c in s:
    for i,v in enumerate(keyboard):
        if c in v:
            x = i
            y = v.index(c)
            break
    l.append(x)
    l.append(y)
    print(keyboard[x][y])
count = 0
print(l)

n = len(l)
for i in range(2,n,2):
    x1 = l[i]
    x2 = l[i-2]
    y1 = l[i+1] 
    y2 = l[i-1]
    count += abs(x1 - x2) + abs(y1 - y2)
    
#    print(keyboard[x][y])
    
print(count)