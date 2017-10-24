import math

#-----------------------------------------------------
#----------------------Functions----------------------
#-----------------------------------------------------

#function to calculate Jukes Cantor distance given p
def JukesCantorCalc(p):
    temp = 1.0 - (4.0 * p / 3.0)
    return (-0.75 * math.log(temp))

#function to calculate the dissimilarity of two strings
def SimCalc(string1, string2):
    x = 0;
    for i in range(0, len(string1)):
        if(string1[i] != string2[i]):
            x+=1       
    return x/(len(string1) * 1.0)

#function to print a matrix with its row/col names
def PrintMatrix(matrix, animalNames):
    row = '\t'
    for i in range (0, len(animalNames)):
        if (len(animalNames[i][0]) < 7):
            row += animalNames[i][0] + '\t'
        else:
           row += animalNames[i][0][:4] + '...\t' 
    print row
    for i in range (0, len(matrix)):
        if (len(animalNames[i][0]) < 7):
            row = animalNames[i][0] + '\t['
        else:
           row = animalNames[i][0][:4] + '...\t['
        for j in range (0, len(matrix[i])):
            row += (str(round(matrix[i][j], 4)) + '\t')
        row += ']'
        print row

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

print '\n'
#set of all matrices and animal names
matrices = []
animalList = []

# init the first distance matrix
distances1 = []
for i in range (0, len(animals)):
    distances1.insert(i, [])
for i in range(0, len(animals)):
    for j in range (0, len(animals)):
        #sometimes the formula returns -0.0, so do absolute value
        temp = abs(JukesCantorCalc(SimCalc(animals[i][1], animals[j][1])))
        distances1[i].insert(j, temp)
#add the first distance to the matrix list
matrices.insert(0, distances1)

# init the first animal names
animalNames1 = []
animalNames1.insert(0, ['dog', 1])
animalNames1.insert(1, ['cat', 1])
animalNames1.insert(2, ['mouse', 1])
animalNames1.insert(3, ['pig', 1])
animalNames1.insert(4, ['human', 1])
#add the first animalnames to the animal names list
animalList.insert(0, animalNames1)

#print the first matrix
PrintMatrix(distances1, animalNames1)
print '\n'

#Iteratively compute the smallest distance, new matrix, and animal names
newSize = len(animals)
oldDistances = distances1
oldAnimalNames = animalNames1
for matrixIter in range (newSize, 2, -1):

    #newSize is the size of the new matrix
    newSize = len(oldAnimalNames)
    #lists to store the new matrix and animal names
    animalNames = []
    distances = []
    
    #find smallest distance and its indices
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

    #create new list of animalNames by combining the two with the smallest distance
    for i in range(0, newSize):
        if(i == smallestI):
            num = oldAnimalNames[smallestI][1] + oldAnimalNames[smallestJ][1]
            animalNames.append([oldAnimalNames[smallestI][0] + oldAnimalNames[smallestJ][0], num])
        elif(i == smallestJ):
            continue
        else:
            animalNames.append([oldAnimalNames[i][0], oldAnimalNames[i][1]])
    animalList.append(animalNames)

    #creates new matrix by combining the two rows/cols with the smallest distance
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
                tempDist2 = oldDistances[smallestI][k] * 1.0
                tempDist3 = (oldAnimalNames[smallestJ][1] * 1.0 / (oldAnimalNames[smallestI][1] * 1.0 + oldAnimalNames[smallestJ][1]) * 1.0)
                tempDist4 = oldDistances[smallestJ][k] * 1.0
                result = (tempDist1 * tempDist2) + (tempDist3 * tempDist4)
                distances[i].insert(j, result)
            else:
                distances[i].insert(j, oldDistances[k][l])
            l+=1
        k+=1
    matrices.append(distances)
    
    #replace the old matrix with the new ones we made
    oldAnimalNames = animalNames
    oldDistances = distances

    #print the new matrix
    PrintMatrix(distances, animalNames)
    print '\n'
        
    
