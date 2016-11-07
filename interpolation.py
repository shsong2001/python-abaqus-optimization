# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 19:53:52 2016

@author: Jens

Input: Set of points
Output: Polynomial fitted to points using the least squares method

"""

import matplotlib.pyplot as plt
import numpy as np
import json

# Read points from io_points.json

with open('io_points.json','r') as f:
    points_y = json.load(f)
    points_x = list(range(len(points_y)))

    
plt.plot(points_y,'ro') # add points to plot


# Calculate interpolated polynomial

p = np.polyfit(points_x, points_y,3) # returns float64 array
function = np.poly1d(p) # generate function from coefficients
p = p.tolist() # convert p back to list for json dump

# Generate function values for plotting
function_x = np.linspace(points_x[0],points_x[-1],50)
function_y = function(function_x)


def savePlotPDF ( filename ):
    "Save the generated plot as a PDF"
    # Must be called before plt.show()!
    # Or use subplots...
    plt.savefig(filename)
    return  
    
def dumpCoeffs ( filename ):
    "Dump coefficients to coeff.json"
    file = open(filename, 'w')
    file.truncate()
    json.dump(plist, file)
        
def plotSetup ():
    "General plot setup"
    plt.axis([-1, 4, 0, 10])
    plt.title("Points and Polynomial Fit")
    plt.ylabel("Radius")
    plt.xlabel("Abstand von x=0 (oben)")
    return

dumpCoeffs('coeffs.json')  

plotSetup()
plt.plot(points_y,'ro') # add points to plot
plt.plot(function_x,function_y) # add polynomial to plot
savePlotPDF('points_polyfit.pdf') 
plt.show()

print(function)


