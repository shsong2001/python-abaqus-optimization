# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:52 2016

@author: Jens

Input: 
    Set of 2 points
Output: 
    Volume of function rotated around x axis
    Coefficents of a polynomial function (ax2+bx+c) fitted to points using the least squares method

Things to edit when changing the number of points
    

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
        
    
def rotationVolume ( function ):
    result = integrate.quad(lambda x: function(x)*function(x),0,2)
    return math.pi*result[0]
    
def istEnformbar ( function, leftbound, rightbound ):
    '''
    Manufacturable only when there are no concave (f''<0) sections
    or in this case (3rd order Polynomial), test for only one zero
    Not well-implemented.
    '''
    function = np.poly1d(function)
    criticalPoints = np.polyder(function).r # returns roots of the derivative
    realCriticalPoints = criticalPoints[criticalPoints.imag==0].real # get real roots
    secondDer = np.polyder(function,2) # calculate second derivative
    testPoints = secondDer(realCriticalPoints) # get values at real roots
    
    crit = np.asarray(realCriticalPoints)
    for i in range(len(crit)):
        if testPoints[i] < 0 & leftbound > crit[i] > rightbound:
            return False
    return True
 
    criticalPoints = np.polyder(function).r # returns roots of the derivative
    realCriticalPoints = criticalPoints[criticalPoints.imag==0].real # get real roots
    secondDer = np.polyder(function,2) # calculate second derivative
    return secondDer(realCriticalPoints) # get values at real roots
    

#==============================================================================
#
# Begin Script
# 
#==============================================================================

# Read data from input.json
with open('input.json','r') as f:
    input = json.load(f)
    input = {'p1': [3,2],'p2': [1,1],'p3': [3,0],'vol':14}
    
keys = ('p1','p2','p3','vol')    
points = [input[keys[i]] for i in range(len(keys)-1)]
volume = input[keys[len(keys)-1]]

# split points into x and y
points_x = [points[i][0] for i in range(len(points))]
points_y = [points[i][1] for i in range(len(points))]

# Calculate interpolated polynomial
p = np.polyfit(points_y, points_x,2) # returns float64 array of coefficients from highest to lowest order
function = np.poly1d(p) # generate function from coefficients
p = p.tolist() # convert p back to a list

# Generate function values for plotting
function_y = np.linspace(points_y[0],points_y[-1],50)
function_x = function(function_y)

# Tests
rotatedVolume = rotationVolume(function)
#functionMin = minV(function)
#functionMax = maxV(function)
#entformbar = istEnformbar(function, 0, 3)

coeffnames = ('a','b','c') # must be same length as p
coeffs = {coeffnames[i]: p[i] for i in range(0,len(p))}
dumpData(coeffs, 'int_output.json')  
#dumpData(inputdata, 'input.json')

# Plots
plt.axis([-5, 5, -5, 5])
plt.title("Points and Polynomial Fit")
plt.ylabel("Abstand von unten")
plt.xlabel("Radius")
plt.vlines(0,0,2,'k','-.')
plt.plot(points_x,points_y,'ro') # add points to plot
plt.plot(function_x,function_y) # add polynomial to plot
#savePlotPDF('points_polyfit.pdf') 
plt.show()

print(function)