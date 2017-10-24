#usage: python tree.pl (A((BC)D)(EF)) > output.ps

import sys, re

#print the required code for postscript file
print '%!PS-Adobe-'
print '%%BoundingBox : atend'
print '/n /newpath load def'
print '/m /moveto load def'
print '/l /lineto load def'
print '/rm /rmoveto load def'
print '/rl /rlineto load def'
print '/s /stroke load def'
print '1.0 setlinewidth 50 100 translate 2 2 scale'
print '/Helvetica findfont 10 scalefont setfont'

#example tree format
#tree = '(A((BC)D)(EF))'

#set the initial state of all variables
tree = sys.argv[1]
#subbedTree removes all excess characters to just get the nodes
subbedTree = re.sub('[()]', '', tree)
xx = {}
yy = {}
x = 0
y = 100

#add each letter to the ps file, with the same y location and decrement x by 20
for nd in range (0, len(subbedTree)):
    print (str(x) + " " + str(y) + " m (" + subbedTree[nd] + ") stringwidth pop -0.5 mul 0 rm (" + subbedTree[nd] + ") show")
    xx[subbedTree[nd]] = x
    x+=20
    yy[subbedTree[nd]] = 90

#workingtree stores the tree that changed based on the loop
workingTree = tree
running = True
while (running):
    #search for the first index of ([A-Z][A-Z])
    searchResult = re.search('\(?([A-Z])([A-Z])\)?', workingTree)
    if searchResult:
        char1 = searchResult.group(1)
        char2 = searchResult.group(2)
        print ("n " + str(xx[char1]) + " " + str(yy[char1]) + " m")
        if (yy[char1] > yy[char2]):
            yy[char1] = yy[char2]
        yy[char1] -= 20
        print (str(xx[char1]) + " " + str(yy[char1]) + " l " + str(xx[char2])
               + " " + str(yy[char1]) + " l " + str(xx[char2]) + " "
               + str(yy[char2]) + " l s")
        xx[char1] = 0.5 * (xx[char1] + xx[char2])
        workingTree = re.sub('\(?([A-Z])([A-Z])\)?', char1, workingTree, 1)
    else:
        running = False
    
print ('n ' + str(xx[workingTree]) + ' ' + str(yy[workingTree])
       + ' m 0 -20 rl s showpage')
rx = 2*x + 30
yt = 2 * yy[workingTree] - 146
print ('%%BoundingBox : 40 95 ' + str(rx) + ' ' + str(yt))
