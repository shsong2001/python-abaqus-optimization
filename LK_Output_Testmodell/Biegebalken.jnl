# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
mdb.models.changeKey(fromName='Model-1', toName='Biegebalken')
mdb.models['Biegebalken'].ConstrainedSketch(name='__profile__', sheetSize=
    200.0)
mdb.models['Biegebalken'].sketches['__profile__'].rectangle(point1=(0.0, 0.0), 
    point2=(-30.0, 20.0))
mdb.models['Biegebalken'].Part(dimensionality=THREE_D, name='Balken', type=
    DEFORMABLE_BODY)
mdb.models['Biegebalken'].parts['Balken'].BaseSolidExtrude(depth=200.0, sketch=
    mdb.models['Biegebalken'].sketches['__profile__'])
del mdb.models['Biegebalken'].sketches['__profile__']
mdb.models['Biegebalken'].Material(name='Stahl')
mdb.models['Biegebalken'].materials['Stahl'].Elastic(table=((210000.0, 0.3), ))
mdb.models['Biegebalken'].HomogeneousSolidSection(material='Stahl', name='All', 
    thickness=None)
mdb.models['Biegebalken'].parts['Balken'].Set(cells=
    mdb.models['Biegebalken'].parts['Balken'].cells.getSequenceFromMask((
    '[#1 ]', ), ), name='Set-1')
mdb.models['Biegebalken'].parts['Balken'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Biegebalken'].parts['Balken'].sets['Set-1'], sectionName='All', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Biegebalken'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Biegebalken'].rootAssembly.Instance(dependent=ON, name='Balken-1', 
    part=mdb.models['Biegebalken'].parts['Balken'])
mdb.models['Biegebalken'].StaticStep(name='Verschiebung', previous='Initial')
mdb.models['Biegebalken'].rootAssembly.Set(faces=
    mdb.models['Biegebalken'].rootAssembly.instances['Balken-1'].faces.getSequenceFromMask(
    ('[#10 ]', ), ), name='Set-1')
mdb.models['Biegebalken'].EncastreBC(createStepName='Verschiebung', localCsys=
    None, name='Fix', region=
    mdb.models['Biegebalken'].rootAssembly.sets['Set-1'])
mdb.models['Biegebalken'].rootAssembly.Set(faces=
    mdb.models['Biegebalken'].rootAssembly.instances['Balken-1'].faces.getSequenceFromMask(
    ('[#20 ]', ), ), name='Set-2')
mdb.models['Biegebalken'].DisplacementBC(amplitude=UNSET, createStepName=
    'Verschiebung', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    localCsys=None, name='Versch', region=
    mdb.models['Biegebalken'].rootAssembly.sets['Set-2'], u1=UNSET, u2=-0.5, 
    u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Biegebalken'].parts['Balken'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=5.0)
mdb.models['Biegebalken'].parts['Balken'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Biegebalken'].parts['Balken'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Biegebalken'].parts['Balken'].generateMesh()
mdb.models['Biegebalken'].rootAssembly.regenerate()
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Biegebalken', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Biegebalken', nodalOutputPrecision=
    SINGLE, numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', 
    type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
# Save by Admin on 2016_11_09-13.30.40; build 6.14-3 2015_02_02-22.17.19 134785
