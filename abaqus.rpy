# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.14-5 replay file
# Internal Version: 2015_08_18-16.37.49 135153
# Run by Jens on Mon Nov 14 15:05:59 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.38281, 1.38426), width=203.55, 
    height=137.319)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execPyFile('C:/SIMULIA/Abaqus/6.14-5/code/python2.7/lib/noGuiInteractive.pyc', 
    __main__.__dict__)
#: Model: C:/GitHub/python-abaqus-optimization/LK_Output_Testmodell/Biegebalken.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       4
#: Number of Node Sets:          4
#: Number of Steps:              1
