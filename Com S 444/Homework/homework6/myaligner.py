import math, random, sys, argparse

#TODO WITH ARGPARSE
parser = argparse.ArgumentParser()
parser.add_argument("echo", )

#Init scores for match, mismatch, and gap penalty
#mismatchScore = sys.argv[2]
#matchScore = sys.argv[4]
#gapPenalty = sys.argv[6]

#REMOVE AFTER TESTING
mismatchScore = -1
matchScore = 1
gapPenalty = -1
seq1 = "TTCGGGAA"
seq2 = "TTCGGCTAC"

#Init sequences and their lengths
#seq1 = sys.argv[7]
#seq2 = sys.argv[8]
if(len(seq1) > len(seq2)):
    temp = seq1
    seq1 = seq2
    seq2 = temp

seq1Len = len(seq1) #this is n
seq2Len = len(seq2) # this is m

#Init matrix
tempList = []
matrix = []

#init first row of the matrix
for i in range(0, seq2Len+1):
    if(i == 0): matrix.insert(i, [0])
    else:matrix.insert(i, [(matrix[i-1][0]+gapPenalty)])
    
#init first col of the matrix
for i in range(1, seq1Len+1): #skip first 0 since it was already inserted
    matrix[0].insert(i, matrix[0][i-1]+gapPenalty);

#init rest of matrix based on first row and col
for i in range (1, seq2Len+1):
    for j in range (1, seq1Len+1):
        
        s = 0
        if(seq2[i-1] == seq1[j-1]): s = matchScore
        else: s = mismatchScore
        
        diagShift = matrix[i-1][j-1] + s
        downShift = matrix[i][j-1] + gapPenalty
        rightShift = matrix[i-1][j] + gapPenalty

        if (diagShift >= downShift and diagShift >= rightShift): matrix[i].insert(j, diagShift)
        elif (downShift >= diagShift and downShift >= rightShift): matrix[i].insert(j, downShift)
        elif (rightShift >= diagShift and rightShift >= downShift): matrix[i].insert(j, rightShift)

print(matrix)

#Rebuild string for output purposes (backwards to start with)
i = seq2Len
j = seq1Len
result = ""
while (i > 0):
    if(j > 0):
        if(matrix[i-1][j-1] >= matrix[i][j-1]):
            result = result + seq1[j-1]
            j = j-1
            i = i-1
        else:
            result = (result + "-")
            i = i-1
    else:
        result = (result + "-")
        i = i-1

print result
