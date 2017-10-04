from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqUtils
import random

mainSeqRecord = SeqIO.parse("NC_000908.gb", "genbank").next()

#to get GC content
print(SeqUtils.GC(mainSeqRecord.seq))

seqString = str(mainSeqRecord.seq)

writeFile = open("randomizedSequences.fasta", "w")

writeString = ""

#write new sequenced to fasta file
for i in range(0,100):
    writeString += ">Seq"+str(i)+"\n"
    writeString += ''.join(random.sample(seqString,len(seqString))) + "\n"

writeFile.write(writeString)

writeFile.close()

#use random for permutations

#getorf gives the orfs

