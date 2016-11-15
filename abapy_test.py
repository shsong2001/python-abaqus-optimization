# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:44:30 2016

@author: Jens

ABAQUS/PYTHON POST PROCESSING SCRIPT
Run using abaqus python / abaqus viewer -noGUI / abaqus cae -noGUI



"""


from odbAccess import openOdb
from abapy.postproc import GetHistoryOutputByKey as gho
#from abapy.misc import dump
from misc import dump_data as dump

from odbMaxMises import getMaxMises

# Setting up some paths
workdir = 'LK_Output_Testmodell'
name = 'Biegebalken'

# Opening the Odb File
odb = openOdb(workdir + '/' + name + '.odb')

# Get max. Mises stress
maxM = getMaxMises(workdir + '/' + name + '.odb','')

dump(maxM,name + '.json')
#dump(maxM, workdir + '/' + name + '.pckl')

# Closing Odb
#odb.close()