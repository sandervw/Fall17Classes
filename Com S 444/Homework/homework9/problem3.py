import re, math

"""
This function calculates standard deviation
Created by David E. Hufnagel on Nov  1, 2017
note: borrowed from code online
"""

#Calculates mean
def Mean(data):
    n = len(data)
    return sum(data)/float(n)

#Return the sum of square deviations of the data
def SS(data):
    c = Mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss
    
#Calculates the standard deviation of the data
def StDev(data):
    n = len(data)
    ss = SS(data)
    pvar = ss/float(n)
    return pvar**0.5

#Calculates the distance between two points
def PointDist(x1, x2, y1, y2, z1, z2):
    xSqr = (x1-x2)**2
    ySqr = (y1-y2)**2
    zSqr = (z1-z2)**2
    result = (xSqr + ySqr + zSqr)**0.5
    return result

def GetAngle(a, b, c):
    num = (a**2) + (b**2) - (c**2)
    den = 2*a*b
    result = math.acos(num/den)
    return result

readFile = open("2gb1.pdb", "r")
writeFile = open("problem2Result.txt", "w")

#sqrt((x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2)

nArr = []
caArr = []
cArr = []

n_caLengths = []
ca_cLengths = []
c_nLengths = []

n_ca_cAngles = []
ca_c_nAngles = []
c_n_caAngles = []

#init atom arrays
index = 0
for line in readFile:
    tempString = line
    strings = re.split(" +", tempString)
    #print (strings[0])
    if(strings[0] == "ATOM"):
        if(strings[2] == "N"):
            nArr.insert(index, [float(strings[6]), float(strings[7]), float(strings[8])])
        elif(strings[2] == "CA"):
            caArr.insert(index, [float(strings[6]), float(strings[7]), float(strings[8])])
        elif(strings[2] == "C"):
            cArr.insert(index, [float(strings[6]), float(strings[7]), float(strings[8])])
        index+=1

for i in range(0, len(nArr)):
    if(i != len(nArr)-1):
        n_caTempLen = PointDist(nArr[i][0], caArr[i][0], nArr[i][1], caArr[i][1], nArr[i][2], caArr[i][2])
        ca_cTempLen = PointDist(caArr[i][0], cArr[i][0], caArr[i][1], cArr[i][1], caArr[i][2], cArr[i][2])
        c_nTempLen = PointDist(cArr[i][0], nArr[i+1][0], cArr[i][1], nArr[i+1][1], cArr[i][2], nArr[i+1][2])

        n_caLengths.insert(i, n_caTempLen)
        ca_cLengths.insert(i, ca_cTempLen)
        c_nLengths.insert(i, c_nTempLen)

        c_n2TempLen = PointDist(cArr[i][0], nArr[i][0], cArr[i][1], nArr[i][1], cArr[i][2], nArr[i][2])
        n_ca2TempLen = PointDist(nArr[i+1][0], caArr[i][0], nArr[i+1][1], caArr[i][1], nArr[i+1][2], caArr[i][2])
        n_ca3TempLen = PointDist(nArr[i+1][0], caArr[i+1][0], nArr[i+1][1], caArr[i+1][1], nArr[i+1][2], caArr[i+1][2])
        ca_c2TempLen = PointDist(caArr[i+1][0], cArr[i][0], caArr[i+1][1], cArr[i][1], caArr[i+1][2], cArr[i][2])

        n_ca_cTempAngle = GetAngle(n_caTempLen, ca_cTempLen, c_n2TempLen)
        ca_c_nTempAngle = GetAngle(ca_cTempLen, c_nTempLen, n_ca2TempLen)
        c_n_caTempAngle = GetAngle(c_nTempLen, n_ca3TempLen, Ca_c2TempLen)



print("N-CA Lengths: Mean = \t" + str(Mean(n_caLengths)) + "\tStdDev = \t" + str(StDev(n_caLengths)))
print("CA-C Lengths: Mean = \t" + str(Mean(ca_cLengths)) + "\tStdDev = \t" + str(StDev(ca_cLengths)))
print("C-N Lengths:  Mean = \t" + str(Mean(c_nLengths)) + "\tStdDev = \t" + str(StDev(c_nLengths)))
    
readFile.close()
writeFile.close()
