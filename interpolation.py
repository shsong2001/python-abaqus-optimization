# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:52 2016

@author: Jens

Input: 
    Set of 2 points
Output: 
    
    Coefficents of a polynomial function (ax2+bx+c) fitted to points using the least squares method
    

"""

#Clear Variables - required for Spyder/IPython
from IPython import get_ipython
get_ipython().magic('reset -sf')
#--------------------------------------------

import matplotlib.pyplot as plt
import scipy.integrate as integrate
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
    json.dump(dataDict, file)
    file.close()
        
    
def calculateVolume ( function ):
    result = integrate.quad(lambda x: function(x),0,2)
    return result[0]
    
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
    

'''
Begin Script
'''

# Read points from io_points.json
with open('io_points.json','r') as f:
    points_y = json.load(f)
    points_x = list(range(len(points_y)))
    inputdata = {'y_1': 3,'y_2': 0,'y_3': 3}

# Calculate interpolated polynomial
p = np.polyfit(points_x, points_y,2) # returns float64 array of coefficients from highest to lowest order
function = np.poly1d(p) # generate function from coefficients
p = p.tolist() # convert p back to a list

# Generate function values for plotting
function_x = np.linspace(points_x[0],points_x[-1],50)
function_y = function(function_x)

# Tests
functionVolume = calculateVolume(function)
#functionMin = minV(function)
#functionMax = maxV(function)
#entformbar = istEnformbar(function, 0, 3)

coeffnames = ('a','b','c') # must be same length as p
coeffs = {coeffnames[i]: p[i] for i in range(0,len(p))}
dumpData(coeffs, 'int_output.json')  

# Plots
plt.axis([-1, 4, 0, 10])
plt.title("Points and Polynomial Fit")
plt.ylabel("Radius")
plt.xlabel("Abstand von x=0 (oben)")
plt.plot(points_y,'ro') # add points to plot
plt.plot(function_x,function_y) # add polynomial to plot
#savePlotPDF('points_polyfit.pdf') 
plt.show()

print(function)

