# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:46:32 2016

@author: Jens
"""
#
#Clear Variables - required for Spyder/IPython
from IPython import get_ipython
get_ipython().magic('reset -sf')
#--------------------------------------------

# Open Abaqus python interface

import os

os.system('abaqus python noGUI=abapy_test.py')

