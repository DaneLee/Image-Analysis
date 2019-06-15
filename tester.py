# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:55:09 2018

@author: Dane
"""

from PIL import Image
import os
from matplotlib import pyplot as plt 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


#Working Function
def convert_Pics(fileName):
    pathS='C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\images\\'
    pathS=pathS+fileName
    pathM='C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\masks\\'
    pathM=pathM+fileName
    m = Image.open(pathS).convert('L')
    n = Image.open(pathM).convert('L')
    M = np.array(m.getdata()).reshape(m.size[0],m.size[1])
    M = np.matrix(M)
    N = np.array(n.getdata()).reshape(n.size[0],n.size[1])
    N = np.matrix(N)
    return [M, N]



#Testing the file
#Average black value function
#M is the matrix of greys
#N is the matrix of black and white
def avg_val_black(M, N):
    salts=[]
    for i in range(len(N)):
        for j in range(len(N.T)):
            if(N[i,j] ==0 ):
                salts.append(M[i,j])
    if len(salts) > 0:
        return [np.mean(salts), np.std(salts)]
    else:
        return 
    

saltIm = os.listdir('C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\images\\')

pointB = []
for i in saltIm:
    if i == '0aabdb423e.png':
        break
    temp = convert_Pics(i)
    pointB.append(avg_val_black(temp[0], temp[1])[0])

avb = []    
for k in range(len(pointB)):
    avb.append(pointB[k])
    
print(np.mean(avb))

plt.hist(avb, bins = 'auto')
#plt.yticks(range(0, 3))
plt.title("Histogram of Average Black Values")
plt.show

#print(avb)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
   