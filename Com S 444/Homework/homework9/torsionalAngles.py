"""
The goal of this script is to calculate one torsional angle (psi) correctly.
Students are asked to calculate psi and phi, and will therefore have to create 
their own calculation for phi based on what is done here with psi. The
torsional angle requires 4 atoms to calculate, and is the angle between the
plane created with the first 3 atoms and the plane created with the last 3 
atoms.  The angle is the torsional angle between the middle 2 atoms.
Created by David E. Hufnagel on Oct, 31 2017

plane calculation reference: http://keisan.casio.com/exec/system/1223596129
angle between planes calculation reference: http://study.com/academy/lesson/dihedral-angle-definition-calculation.html
"""
import math

#set coordinates (these coordinates are rounded values from the second aa in 2GB1)
Clast = (-11.8,0.3,4.2)  
Ncur = (-11.1,-0.6,4.7)
CAcur = (-9.7,-0.4,5.0)
Ccur = (-8.9,-1.6,4.4)

#calculate plane formulas
##plane 1
a1 = (CAcur[1]-Ncur[1])*(Clast[2]-Ncur[2])-(Clast[1]-Ncur[1])*(CAcur[2]-Ncur[2])
b1 = (CAcur[2]-Ncur[2])*(Clast[0]-Ncur[0])-(Clast[2]-Ncur[2])*(CAcur[0]-Ncur[0])
c1 = (CAcur[0]-Ncur[0])*(Clast[1]-Ncur[1])-(Clast[0]-Ncur[0])*(CAcur[1]-Ncur[1])
d1 = -1.0*(a1*Ncur[0]+b1*Ncur[1]+c1*Ncur[2])
#plane1 = a1x+b1y+c1z+d1

##plane 2
a2 = (Ccur[1]-CAcur[1])*(Ncur[2]-CAcur[2])-(Ncur[1]-CAcur[1])*(Ccur[2]-CAcur[2])
b2 = (Ccur[2]-CAcur[2])*(Ncur[0]-CAcur[0])-(Ncur[2]-CAcur[2])*(Ccur[0]-CAcur[0])
c2 = (Ccur[0]-CAcur[0])*(Ncur[1]-CAcur[1])-(Ncur[0]-CAcur[0])*(Ccur[1]-CAcur[1])
d2 = -1.0*(a1*CAcur[0]+b1*CAcur[1]+c1*CAcur[2])
d1 = -1.0*(a1*Ncur[0]+b1*Ncur[1]+c1*Ncur[2])
#plane2 = a2x+b2y+c2z+d2

#calculate torsional angle between planes
top = a1*a2+b1*b2+c1*c2
bottom = math.sqrt(a1**2+b1**2+c1**2)*math.sqrt(a2**2+b2**2+c2**2)
psiAngle = math.degrees(math.acos(top/bottom))
