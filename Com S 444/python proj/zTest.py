import random
import math

#simulate z Value from other values
#-------------------------------------
n = 10
u0 = 3
o = 1
randSum = 0

randList = []

for i in range(0, n):
    #random.gauss takes mean and stdDev as arguments
    randList.insert(i, random.gauss(u0, o))
    print randList[i]
    randSum = randSum + randList[i]

randMean = randSum/n

zValue = (randMean - 3) / (o / (n ** 0.5))

print zValue

#Simulate z value directly (z ~ N(mean, stdDev))
#z has standard normal distribution
#-------------------------------------

zValue = random.gauss(0, 1)
print zValue
