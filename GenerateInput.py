# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:55:31 2016

@author: Jens
"""
# Clear Variables - required for Spyder/IPython
from IPython import get_ipython
get_ipython().magic('reset -sf')
#==============================================================================

from abapy.mesh import nodes


'''
# Setting up some paths
workdir = 'LK_Output_Testmodell'
file_orig = 'Biegebalken_orig.inp'

f = open(file_orig,'r')
inp = f.read()
f.close()

'''

labels = range(5)

# Node list
i = 101
y=0
for x in range(nodes_x):
    print('{0:2d}, {1:2d}., {2:2d}., {3:2d}.'.format(i, x, y, 0))
    i += 1
y=1
for x in range(nodes_x-1):
    print('{0:2d}, {1:2d}., {2:2d}., {3:2d}.'.format(i, x, y, 0))
    i += 1
    
# Element list
i = 11
y=0
for x in range(nodes_x):
    print('{0:2d}, {1:2d}, {2:2d}'.format(i, x, y))
    i += 1