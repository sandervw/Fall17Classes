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
    
test = [10,2,38,23,38]
stdev = StDev(test)
print stdev