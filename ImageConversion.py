# -*- coding: utf-8 -*-
"""
Sage to Python Conversion

@author: Dane
"""

#Packages
from PIL import Image
import os
from matplotlib import pyplot as plt 
import numpy as np


#Main Body of Program


"""This functions opens the pictures
   and converts all the pixels into
   integer values based on their greyscale
   value from 0 to 255 or black to white.
"""
#Image Open and Conversion Function
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

"""These functions takes as their arguments
   two matrices and loops through all
   values of the second matrix input.
   The functions go through the rows
   of the matrix just by the "len(matrix)"
   command and goes through the colums by 
   the "len(matrix.transpose)" command.
   The function then checks if the pixel value
   is "0 for avg_val_black function" or "255 for
   avg_val_white function" and appends the pixel 
   at that position in the first matrix to an 
   array created within the function.
   The function then returns the mean and standard
   deviation of the array.
"""
#Average black value function
#M is the matrix of greys
#N is the matrix of black and white
def avg_val_black(M, N):
    salts=[]
    for i in range(len(N)):
        for j in range(len(N.T)):
            if(N[i,j] == 0):
                salts.append(M[i,j])
    if len(salts) > 0:
        return [np.mean(salts), np.std(salts)]
    else:
        return

#Average white value function
#M is the matrix of greys
#N is the matrix of black and white
def avg_val_white(M, N):
    salts=[]
    for i in range(len(N)):
        for j in range(len(N.T)):
            if(N[i,j] == 255):
                salts.append(M[i,j])
    if len(salts) > 0:
        return [np.mean(salts), np.std(salts)]
    else:
        return


"""This line creates a variable that holds file
   path to the folders containing the images
   and mask that will be looped through.
"""
#Image and Mask File Path
salt_images = os.listdir('C:\\Users\\Dane\\Documents\\MathResearch\\all\\train\\images\\')

"""The function below loops through the
   uses the "convert_Pics" fucntion to 
   open the images and mask. The functions
   return the mean values of the images
   based on their greyscale value of black
   or white.
"""
#Image computation fucntion
pointB = []
for i in salt_images:
    temp = convert_Pics(i)
    pointB.append(avg_val_black(temp[0], temp[1])[0])
avb = []    
for k in range(len(pointB)):
    avb.append(pointB[k])

print("This is the mean average black values:")
print(np.mean(avb))

#Image computation fucntion
pointW = []
for i in salt_images:
    temp = convert_Pics(i)
    pointW.append(avg_val_white(temp[0], temp[1])[0])
avw = []    
for k in range(len(pointW)):
    avw.append(pointW[k])

#print("This is the mean average white values:")
#print(np.mean(avw))








