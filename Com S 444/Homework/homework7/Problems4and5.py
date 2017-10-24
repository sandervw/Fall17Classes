import math

def JukesCantorCalc(p):
    temp = 1.0 - (4.0 * p / 3.0)
    return (-0.75 * math.log(temp))

def SimCalc(string1, string2):
    x = 0;
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            x+=1
        
    return x/(len(string1) * 1.0)

#-----------------------------------------------------
#----------------------Problem 4----------------------
#-----------------------------------------------------

animals = []

animals.insert(0, ['dog', 'ATGACCAACATTCGAAAAACCCACCCACTA'])
animals.insert(1, ['cat', 'ATGACCAACATTCGAAAATCACACCCCCTT'])
animals.insert(2, ['mouse', 'ATGACAAACATACGAAAAACACACCCATTA'])
animals.insert(3, ['pig', 'ATGACCAACATCCGAAAATCACACCCACTA'])
animals.insert(4, ['human', 'ATGACCCCAATACGCAAAACTAACCCCCTA'])

for i in range(0, len(animals)):
    for j in range (i+1, len(animals)):
        temp = JukesCantorCalc(SimCalc(animals[i][1], animals[j][1]))
        print ('Distance between ' + animals[i][0] + ' and ' + animals[j][0]
               + ' is:\t'+ str(temp))

#-----------------------------------------------------
#----------------------Problem 5----------------------
#-----------------------------------------------------

#set of all matrices and animal names
matrices = []
animalList = []

#set of all distances (varies based on level)
distances1 = []

# init the first distance matrix
for i in range (0, len(animals)):
    distances1.insert(i, [])
for i in range(0, len(animals)):
    for j in range (0, len(animals)):
        temp = JukesCantorCalc(SimCalc(animals[i][1], animals[j][1]))
        distances1[i].insert(j, temp)

print distances1

#add the first distance to the matrix
matrices.insert(0, distances1)

animalNames1 = []
animalNames1.insert(0, ['dog', 1])
animalNames1.insert(1, ['cat', 1])
animalNames1.insert(2, ['mouse', 1])
animalNames1.insert(3, ['pig', 1])
animalNames1.insert(4, ['human', 1])

animalList.insert(0, animalNames1)

# iteratively compute the new matrix
newSize = len(animals)
oldDistances = distances1
oldAnimalNames = animalNames1
for matrixIter in range (newSize, 2, -1):

    newSize = len(oldAnimalNames)
    animalNames = []
    distances = []
    
    
    #find smallest distance
    smallest = 1
    smallestI = 0
    smallestJ = 0
    for i in range(0, newSize):
        for j in range(0, newSize):
            if (i != j):
                if(oldDistances[i][j] < smallest):
                    smallest = oldDistances[i][j]
                    smallestI = i
                    smallestJ = j

    #create new list of animalNames
    for i in range(0, newSize):
        if(i == smallestI):
            num = oldAnimalNames[smallestI][1] + oldAnimalNames[smallestJ][1]
            animalNames.append([oldAnimalNames[smallestI][0] + oldAnimalNames[smallestJ][0], num])
        elif(i == smallestJ):
            continue
        else:
            animalNames.append([oldAnimalNames[i][0], oldAnimalNames[i][1]])
    print animalNames
    animalList.append(animalNames)

    #creates new matrix
    for i in range (0, len(animalNames)):
        distances.insert(i, [])
    k = 0
    l = 0
    for i in range(0, len(animalNames)):
        l = 0
        for j in range (0, len(animalNames)):
            if (k == smallestJ):
                k+=1
            if(l == smallestJ):
                l+=1
            if (i == j):
                distances[i].insert(j, 0.0)
            elif(k == smallestI):
                tempDist1 = (oldAnimalNames[smallestI][1] * 1.0 / (oldAnimalNames[smallestI][1] * 1.0 + oldAnimalNames[smallestJ][1]) * 1.0)
                tempDist2 = oldDistances[smallestI][l] * 1.0
                tempDist3 = (oldAnimalNames[smallestJ][1] * 1.0 / (oldAnimalNames[smallestI][1] * 1.0 + oldAnimalNames[smallestJ][1]) * 1.0)
                tempDist4 = oldDistances[smallestJ][l] * 1.0
                result = (tempDist1 * tempDist2) + (tempDist3 * tempDist4)
                distances[i].insert(j, result)
            elif(l == smallestI):
                tempDist1 = (oldAnimalNames[smallestI][1] * 1.0 / (oldAnimalNames[smallestI][1] * 1.0 + oldAnimalNames[smallestJ][1]) * 1.0)
                tempDist2 = oldDistances[smallestI][l] * 1.0
                tempDist3 = (oldAnimalNames[smallestJ][1] * 1.0 / (oldAnimalNames[smallestI][1] * 1.0 + oldAnimalNames[smallestJ][1]) * 1.0)
                tempDist4 = oldDistances[smallestJ][l] * 1.0
                result = (tempDist1 * tempDist2) + (tempDist3 * tempDist4)
                distances[i].insert(j, result)
            else:
                distances[i].insert(j, oldDistances[k][l])
            l+=1
        k+=1
    print distances
    matrices.append(distances)
    
    oldAnimalNames = animalNames
    oldDistances = distances
        
    
