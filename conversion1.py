# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:25:51 2018

@author: Dane
"""

#Importing Libraries
from PIL import Image
import cv2.cv as cv
import numpy as np
import matplotlib.pyplot as plt
import os



#This is a test to make sure the program runs
print("this is a test")

#I will start the actually program here

#Functions

#Average white value function
#M is the matrix of greys
#N is the matrix of black and white
def avg_val_white(M, N):
    salts = []
    for i in range(N[:, 0]):
        for j in range(N[:, [0]]):
            if(N[i,j] == 255):
                salts.append(M[i,j])
    if(len(salts) > 0):
        return [np.mean(salts), np.std(salts)]
    else:
        return
    
#Average black value function
#M is the matrix of greys
#N is the matrix of black and white
def avg_val_black(M, N):
    salts = []
    for i in range(N[:, 0]):
        for j in range(N[:, [0]]):
            if(N[i,j] == 0):
                salts.append(M[i,j])
    if(len(salts) > 0):
        return [np.mean(salts), np.std(salts)]
    else:
        return

#File handling function
def open_pics(fileName):
    pathS='C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\images\\'
    pathS=pathS+fileName
    pathM='C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\masks\\'
    pathM=pathM+fileName
    m=Image.open(pathS)
    m=m.convert('L')
    n=Image.open(pathM)
    n=n.convert('L')
    M=np.array(m.getdata()).reshape(m.size[0],m.size[1])
    #M=Matrix(RR,M)
    N=np.array(n.getdata()).reshape(n.size[0],n.size[1])
    #N=Matrix(RR,N)
    return [M,N]
#file line
saltFile = os.listdir('C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\images\\')

#test functions

pointsB = []
for f in saltFile:
    temp = open_pics(f)
    pointsB.append(avg_val_black(temp[0], temp[1]))

def plot_test():
    plt.plot(pointsB, color = "red")
    plt.show()

print("time to test")