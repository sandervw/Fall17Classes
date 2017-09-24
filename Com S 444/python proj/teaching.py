#Geric script

import math
import random

#Operators
#   ** = exp
#   % = mod
#   // = floor division
#Area = 4*pi*r^2

r = 5.2
sphereArea = 4*math.pi * r**2

s = 'testString'
    
print(sphereArea)
print(s[2]) #prints 3rd char
print(s[1:4]) #prints chars 2 through 4
print(s[1:4:2]) #prints chars 2 through 4, but skips every other char

#method: input.method(paramA, paramB)
#function: method(input, paramA, paramB)

#s.strip("string") = remove argument from the start and end of the string
#s.split("string") = split string into pieces based on argument
#default for both is whitespace
print(s.strip("t"));
print(s.split("t"));

#len(string) returns the length
#s.count("string") counts the number of times argument appears in the string

#to cast data types, do str(obj) int(obj), or float(obj)

#for python, lsit is coll of obj, matrix is list of lists
#   myList = [1, "hello", 3.2, [1, "t2", 2.3]]
#   + can concat lists, * can be used to repeat a list
#   myList.append(item) adds item to list (if it is a list, puts the entire list as the last item)
#   myList.extend(item) adds item to list(if it is a list, adds list to current list)
#   some list methods:
#       sort() sorts the list from smallest to largest for ints or floats (strings are alphabetical)
#       count(item)
#       index(item) (first occur in list)
#       insert(index, item)
#       remove(item) (first occur)
#       string.join(list) (converts list to string by concating all objects with string as a seperator)
#       len(myList)
#       min(myList), max(myList), sum(myList)

#Example 3
geneList = []
geneList.append([552, "GeneA"]);
geneList.append([1499, "GeneB"]);
geneList.append([1160, "GeneC"]);
geneList.append([478, "GeneD"]);
geneList.sort();
print geneList


#a dictionary is a collection of objects of any kind, structured as keys and values
#   dicX = {'a':'alpha', ''o':'omega', 'g':'gamma'}
#   to add item, dicX[key] = value
#   to get items, dicX[key]
#   Methods:
#       del dicX[key] removes key and value from dict.
#       dicX.update(dicY) adds all of dicY key-value pairs to dicX
#       len(dicX) returns number of keys is dicX
#       also have .keys(), .values(), and .items() to get those

#conditionals
#   if condition:
#       if_Statement
#   elif condition:
#       elif_statement
#   else condition:
#       else_Statement

seqA = "AGGAAUCNACG"
seqB = "AUGUUAACANN"

if seqA[0:3] == "AUG":
    print "Seq A is a protein."
else:
    print "Seq A is not a protein."

if seqB[0:3] == "AUG":
    print "Seq B is a protein."
else:
    print "Seq B is not a protein."

#For loops:
#   for i in range(0,8): #range works as range(start, stop, step)
#       statement
#'continue' restarts the for loop, 'break' ends the for loop

translator = {"UUA":"Leu", "CUG":"Leu", "CGC":"Arg", "AGG":"Arg", 
              "AAU":"Asn", "AUG":"Met", "ACA":"Thr", "GGG":"Gly",}

SeqA = "AGGAAUCUGCGC"
SeqB = "AUGUUAACAGGG"

seqList = [SeqA, SeqB]

resultList = []

for seq in seqList:
    if seq.startswith("AUG"):
        tempString = ""
        for i in range(0, len(seq), 3):
            tempString = tempString + translator[seq[i:i+3]]
        print tempString

#random library for random vars
#   random.choice(list/string) randomly choose one item from list/string
#   random.choice(list/string, k) randomly choose k items from list
#   random.randrange(start, stop) randomly choose int
#   random.uniform(start, stop) randomly choose float

for i in range(0, 100):
    xCoord = random.uniform(-1.0, 1.0)
    yCoord = random.uniform(-1.0, 1.0)
    distance = ((xCoord**2) * (yCoord**2))**(.5)
    if distance <= 1.0:
        print xCoord
        print yCoord
        break

#dynamic input/output
#   can be done using sys library
#   two functions: dynamic I/O, sys.exit()
#   use sys.argv[1], argv[2], etc... (argv[0] is the script running)
#   example: python scriptName arg1, arg2
#   script could be myFile = open(sys.argv[1])

#functions
#   syntax: def FunctionName(paramA, ParamB):
#       do work
#       return object(s)
