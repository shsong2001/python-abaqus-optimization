# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:52 2016

@author: Jens

Input:
    Set of 2 points
Output:
    Volume of function rotated around x axis
    Coefficents of a polynomial function (ax2+bx+c) fitted to points using the least squares method
    
"""

#Clear Variables - required for Spyder/IPython
from IPython import get_ipython
get_ipython().magic('reset -sf')
#--------------------------------------------


#==============================================================================
#
# Imports/Functions
#
#==============================================================================

import matplotlib.pyplot as plt
import scipy.integrate as integrate
import math
import numpy as np
import json


def minV ( function ) :
    function = np.poly1d(function)
    criticalPoints = np.polyder(function).r
    realCriticalPoints = criticalPoints[criticalPoints.imag==0].real # get real roots
    return function(min(realCriticalPoints))

def maxV ( function ) :
    function = np.poly1d(function)
    criticalPoints = np.polyder(function).r
    realCriticalPoints = criticalPoints[criticalPoints.imag==0].real # get real roots
    return function(max(realCriticalPoints))

def savePlotPDF ( filename ):
    "Save the generated plot as a PDF"
    # Must be called before plt.show()!
    # Or use subplots...
    plt.savefig(filename)
    return

def dumpData ( dataDict, filename ):
    "Dump coefficients to file"
    file = open(filename, 'w')
    file.truncate()
    json.dump(dataDict, file, sort_keys=True)
    file.close()


def func_rotationVolume ( function ):
    "Return volume from rotation around x-axis"
    result = integrate.quad(lambda x: function(x)*function(x),0,2)
    return math.pi*result[0]

def poly_rotationVolume (x,y):
    "Generate interpolated polynomial from points and return volume from rotation around x-axis"
    p = np.polyfit(x, y,2) # returns float64 array of coefficients from highest to lowest order
    function = np.poly1d(p) # generate function from coefficients
    return func_rotationVolume(function)


#==============================================================================
#
# Begin Script
#
#==============================================================================

# Read data from input.json
with open('input.json','r') as f:
    input = json.load(f)
    # Uncomment below to overwrite inputfile
    #input = {'p1': [0,13],'p2': [1,10],'p3': [2,18],'vol':14}
    #

keys = ('p1','p2','p3','vol')
points = [input[keys[i]] for i in range(len(keys)-1)]
target_volume = input[keys[len(keys)-1]]

# split points into x and y
points_x = [points[i][0] for i in range(len(points))]
points_y = [points[i][1] for i in range(len(points))]

# Calculate interpolated polynomial
p = np.polyfit(points_x, points_y,2) # returns float64 array of coefficients from highest to lowest order
function = np.poly1d(p) # generate function from coefficients

# Test Volume
rotated_volume = func_rotationVolume(function)

# loop to hit target volume by adjusting radius of point 3
new_points_y = points_y[:] # duplicate the list of points
new_vol = rotated_volume

if rotated_volume > target_volume:
    while (new_vol > target_volume):
        new_points_y[2] -= 1
        new_vol = poly_rotationVolume(points_x,new_points_y)
else:
    while (new_vol < target_volume):
        new_points_y[2] += 1
        new_vol = poly_rotationVolume(points_x,new_points_y)

volume_error = new_vol - target_volume

# Recalculate interpolated polynomial with new points
p = np.polyfit(points_x, new_points_y,2) # returns float64 array of coefficients from highest to lowest order
new_function = np.poly1d(p) # generate function from coefficients


# Write data to json
p = p.tolist() # convert p back to a list for dump
coeffnames = ('a','b','c') # must be same length as p
coeffs = {coeffnames[i]: p[i] for i in range(0,len(p))}
dumpData(coeffs, 'output.json')

#==============================================================================
#
#Plotting
#==============================================================================

# Generate function values for plotting
function_x = np.linspace(points_x[0],points_x[-1],50)
function_y = function(function_x)
new_function_y = new_function(function_x)

# Plots
plt.axis([-1, 3, -20, 30])
plt.title("Points and Polynomial Fit")
plt.ylabel("Radius")
plt.hlines(0,0,2,'k','-.')
plt.plot(points_x,points_y,'r+') # add points to plot
plt.plot(points_x,new_points_y,'ro') # add new points to plot
plt.plot(function_x,function_y,'b--') # add polynomial to plot
plt.plot(function_x,new_function_y,'g') # add new polynomial to plot
plt.plot(function_x,-new_function_y,'g') # add negativ side
#savePlotPDF('points_polyfit.pdf')
plt.show()

print(function)
