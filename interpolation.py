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

# Read points from var.py
from io_points import points

# get x and y vectors
points_x = points[:,0]
points_y = points[:,1]


plt.plot(points_y,'ro') # add points to plot


# Calculate interpolated polynomial

p = np.polyfit(points_x, points_y,3)
function = np.poly1d(p)

plist = p.tolist()

# Generate function values for plotting
function_x = np.linspace(points_x[0],points_x[-1],50)
function_y = function(function_x)



def savePlotPDF ( filename ):
    "Save the generated plot as a PDF"
    # Must be called before plt.show()!
    # Or use subplots...
    plt.savefig(filename)
    return

def writeCoeffs ( filename ):
    "Write coefficients to coeff.txt from highest to lowest order"
    file = open(filename, 'w')
    file.truncate()
    for coeff in p:
        file.write('%.3f' % coeff)
        file.write(",")
    file.close
    return
    
    
def dumpCoeffs ( filename ):
    "Dump coefficients to coeff.txt (JSON)"
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


writeCoeffs('coeffs.csv')  


plotSetup()


plt.plot(points_y,'ro') # add points to plot
plt.plot(function_x,function_y) # add polynomial to plot
savePlotPDF('points_polyfit.pdf') 
plt.show()

print(function)


