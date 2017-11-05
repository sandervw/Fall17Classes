import re

readFile = open("2gb1.pdb", "r")
writeFile = open("problem2Result.txt", "w")

#

for line in readFile:
    tempString = line
    strings = re.split(" +", tempString)
    #print (strings[0])
    if(strings[0] == "ATOM"):
        if(strings[2] == "N" or strings[2] == "CA" or strings[2] == "C"):
            writeFile.write(strings[5] + "\t" + strings[1] + "\t" + strings[2] + "\t" + strings[6] + "\t" + strings[7] + "\t" + strings[8] + "\n")

readFile.close()
writeFile.close()
