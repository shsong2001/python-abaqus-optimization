# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:55:31 2016

@author: Jens
"""
# Clear Variables - required for Spyder/IPython
from IPython import get_ipython
get_ipython().magic('reset -sf')
#==============================================================================

from abapy.mesh import Mesh, Nodes


'''
# Setting up some paths
workdir = 'LK_Output_Testmodell'
file_orig = 'Biegebalken_orig.inp'

f = open(file_orig,'r')
inp = f.read()
f.close()

'''

# create nodes
labels = [1,2,3,4,5]

x = [0.,1.,2.,0.5,1.5]
y = [0.,0.,0.,0.866,0.866]
z = [0.,0.,0.,0.,0.]

sets = {'mynodes': [1,2,3,4,5]}

nodes = Nodes(labels = labels, x = x, y = y, z = z, sets = sets)
print(nodes)

mesh = Mesh()

# create mesh