import math, random, numpy

#Nt is Poisson(lambdaT), Nn is Poisson(lambdaN)
#lambda is the expected value (mean)
#lambda should be the same for both if the gene is not related to SCLC
#IE. lambdaT = lambdaN = lambda
#in this case, lambda is the mean of all the data points
#T = Nt - Nn
#numpy.random.poisson(lambda, size)

#OUTLINE
#---------------
#input set of data T for Poisson(lambdaT)
#input set of data N for Poisson(lambdaN)
#Calculate lambda  = (sum(T)+sum(N)) / (num(T)+num(N))
#generate Nt = random Poisson of lambdaT
#generate Nn = random Poisson of lambdaN
#print Nt- Nn

dataT = [28]
dataN = [13]

#tLambda = sum(dataT) / len(dataT)
#nLambda = sum(dataN) / len(dataN)

mainLambda = (sum(dataT)+sum(dataN)) / (len(dataT)+len(dataN))

Nt = numpy.random.poisson(mainLambda, 1)
Nn = numpy.random.poisson(mainLambda, 1)

print(Nt - Nn)

