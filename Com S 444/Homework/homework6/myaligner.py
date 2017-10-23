import math, random, sys, argparse


#Init scores for match, mismatch, and gap penalty
mismatchScore = int(sys.argv[2])
matchScore = int(sys.argv[4])
gapPenalty = int(sys.argv[6])

#REMOVE AFTER TESTING
#mismatchScore = -1
#matchScore = 1
#gapPenalty = -1
#seq1 = "TTCGGGAA"
#seq2 = "TTCGGCTAC"
#alightment = 1
#matrix = 1

#Init sequences and their lengths
seq1 = sys.argv[7]
seq2 = sys.argv[8]
alignment = int(sys.argv[9])
matrix = int(sys.argv[10])



if(len(seq1) > len(seq2)):
    temp = seq1
    seq1 = seq2
    seq2 = temp

seq1Len = len(seq1) #this is n
seq2Len = len(seq2) # this is m

#Init matrix
matrix = []

#init first row of the matrix
for i in range(0, seq2Len+1):
    if(i == 0): matrix.insert(i, [[0, 'right']])
    else:matrix.insert(i, [[(matrix[i-1][0][0]+gapPenalty), 'right']])
    
#init first col of the matrix
for i in range(1, seq1Len+1): #skip first 0 since it was already inserted
    matrix[0].insert(i, [matrix[0][i-1][0]+gapPenalty, 'down']);

#init rest of matrix based on first row and col
for i in range (1, seq2Len+1):
    for j in range (1, seq1Len+1):
        
        s = 0
        if(seq2[i-1] == seq1[j-1]): s = matchScore
        else: s = mismatchScore
        
        diagShift = matrix[i-1][j-1][0] + s
        downShift = matrix[i][j-1][0] + gapPenalty
        rightShift = matrix[i-1][j][0] + gapPenalty

        if (diagShift >= downShift and diagShift >= rightShift): matrix[i].insert(j, [diagShift, 'diag'])
        elif (downShift >= diagShift and downShift >= rightShift): matrix[i].insert(j, [downShift, 'down'])
        elif (rightShift >= diagShift and rightShift >= downShift): matrix[i].insert(j, [rightShift, 'right'])

print "\nMatrix:"
print(matrix)

#Rebuild string for output purposes (backwards to start with)
i = seq2Len
j = seq1Len
result1 = ""
result2 = ""
while (i > 0):
    if(j > 0):
        if(matrix[i][j][1] == 'diag'):
            result1 = result1 + seq1[j-1]
            result2 = result2 + seq2[i-1]
            j = j-1
            i = i-1
        elif (matrix[i][j][1] == 'right'):
            result1 = (result1 + "-")
            result2 = result2 + seq2[i-1]
            i = i-1
        elif (matrix[i][j][1] == 'down'):
            result2 = (result2 + "-")
            result1 = result1 + seq1[j-1]
            j = j-1
    else:
        result1 = (result1 + "-")
        result2 = result2 + seq2[i-1]
        i = i-1

result1 = result1[::-1]
result2 = result2[::-1]

print "\nAlignment:"
print result1
print result2

print "\nAlignment Cost:"
print matrix[seq2Len][seq1Len][0]
