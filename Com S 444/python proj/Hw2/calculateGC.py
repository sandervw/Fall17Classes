import sys
import math

#FUNCTION for calculating GC content
def CalcGC(chromString):

    #variables to keep track of g and c counts
    gCount = 0
    cCount = 0
    totalCount = 0.0
    
    #go through list searching for G and C elements
    for i in range(len(chromString)):
        if chromString[i] == "G":
            gCount = gCount + 1
            totalCount = totalCount + 1   
        elif chromString[i] == "C":
            cCount = cCount + 1
            totalCount = totalCount + 1
        elif chromString[i] == "A":
            totalCount = totalCount + 1
        elif chromString[i] == "T":
            totalCount = totalCount + 1

    gcContent = (cCount + gCount) / totalCount

    return gcContent


readFile = open(sys.argv[1], "r")
writeFile = open(sys.argv[2], "w")

chromString = ""

for line in readFile:

    tempString = line
    if tempString.startswith(">"):
        #if tempString isnt empty, calculate the GC and write it
        #then write the name on a new line
        if chromString != "":
            writeFile.write(str(CalcGC(chromString)))
            writeFile.write("\n")
            chromString = "" #reset chromeString
            chromName = tempString.strip()
            writeFile.write(chromName)
            writeFile.write("\t")
        #else it is the first line, just write the name
        else:
            chromName = tempString.strip()
            writeFile.write(chromName)
            writeFile.write("\t")
    else:
        chromString = chromString + tempString

writeFile.write(str(CalcGC(chromString)))
writeFile.write("\n")


readFile.close()
writeFile.close()

        

