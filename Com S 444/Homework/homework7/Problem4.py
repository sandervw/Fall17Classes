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

#set of all matrices
matrices = []

#set of all distances (varies based on leve
distances = []

# init the first distance matrix
for i in range (0, len(animals)):
    distances.insert(i, [])
for i in range(0, len(animals)):
    for j in range (0, len(animals)):
        temp = JukesCantorCalc(SimCalc(animals[i][1], animals[j][1]))
        distances[i].insert(j, temp)

#add the first distance to the matrix
matrices.insert(0, distances)

newSize = len(animals)

#find smallest distance
smallest = 1
smallestX = 0
smallestY = 0
for i in range(0, newSize):
    for j in range(0, newSize):
        if (i != j):
            if(distances[i][j] < smallest):
                smallest = distances[i][j]
                smallestY = i
                smallestX = j

print smallest
print smallestX
print smallestY
