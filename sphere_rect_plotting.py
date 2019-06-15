# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:17:28 2019

@author: Dane
"""
"""
Contains the functions for plotting the coordinates on sphere 
and converting from spherical to rectangular coordinates.
The aim is to turn all the code into different sets of functions 
so the user only needs to input very little data.
"""


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random
import math

#Computes the euclidean distance.
def euclid_dist(a):
    dist = ((a[0]) ** 2) + ((a[1]) ** 2) + ((a[2]) ** 2)
    dist = np.sqrt(dist)
    return dist

#Computes the unit vector.
def unit_vector(a):
    if euclid_dist(a) == 0:
        return 0
    else:
        temp = a / (euclid_dist(a))
        return temp

#Computes the postive angle between the z-axis and the vector.    
def phi(a):
    if(a[2] == 0):
        angle = (math.pi) / 2
    else:
        angle = np.sqrt(((a[0]) ** 2) + ((a[1]) ** 2))
        angle = angle / (a[2])
        angle = math.atan(angle)
    return angle

#Computes the angle around the z-axis on the xy-plane.
def theta(a):
    angle = abs(a[1])
    if(a[0] == 0):
        if(a[1] < 0):
            angle = (3 * math.pi) / 2
        elif(a[1] > 0):
            angle = math.pi / 2
    elif(a[1] == 0):
        if(a[0] < 0):
            angle = math.pi
        elif(a[0] > 0):
            angle = 0
    else:
        angle = angle / abs((a[0]))
        angle = math.atan(angle)
        if(a[0] < 0):
            angle = (math.pi / 2) + angle
    return angle

#Plots the given cordinates on a sphere.
def plot_sphere(L):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    for i in range(len(L)):
        temp = unit_vector(L[i])
        ax.scatter(temp[0], temp[1], temp[2], c = 'b', marker = '.')
    plt.show()

#Converts and plots spherical coordinates on a rectangle.
def plot_rect(L):    
    for i in range(len(L)):
        temp = L[i]
        val_phi = phi(temp)
        val_theta = theta(temp)
        plt.scatter(val_theta, val_phi, c = 'r', marker = '.')
    plt.show()


#Test list of random vectors.    
T = [random.sample(range(-100, 100), 3) for i in range(1)]


#Plotting the sphere and rectangle for testing
#plot_sphere(T)
#plot_rect(T)
