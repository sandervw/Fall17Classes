readFile = open("hw2/hw2Seqs.fasta", "r")
writeFile = open("hw2/hw2SeqsDecoded.fasta", "w")

translator = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

for line in readFile:
    tempString = line
    resultString = ""
    if tempString.startswith(">"):
        writeFile.write(tempString)
        continue
    else:
        i = 0
        startDecoding = False
        for i in range(0,len(tempString)):
            if tempString[i:i+3] == "AUG":
                startDecoding = True
                resultString = translator[tempString[i:i+3]]
                break
        for i in range(0,len(tempString), 3):
            if tempString[i:i+3] in ["UAA", "UGA", "UAG"]:
                break;

            if startDecoding:
                resultString = resultString + translator[tempString[i:i+3]]
    resultString = resultString + "\n"
    writeFile.write(resultString)

readFile.close()
writeFile.close()

