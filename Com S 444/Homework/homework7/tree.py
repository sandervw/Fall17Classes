#usage: echo '((((((SL)(BR))W)D)C)M)' | drawtree.pl > output.ps

import sys, re


print '%!PS-Adobe-'
print '%%BoundingBox : atend'
print '/n /newpath load def'
print '/m /moveto load def'
print '/l /lineto load def'
print '/rm /rmoveto load def'
print '/rl /rlineto load def'
print '/s /stroke load def'
print '1.0 setlinewidth 50 100 translate 2 2 scale /Helvetica findfont 10 scalefont setfont'

tree = '((((((SL)(BR))W)D)C)M)'

#tree = sys.argv[1]
subbedTree = re.sub('[()]', '', tree)
xx = []
yy = []
x = 0
y = 0

#print tree
#print subbedTree

for nd in range (0, len(subbedTree)):
    print (str(x) + " " + str(y) + " m (" + subbedTree[nd] + ") stringwidth pop -0.5 mul 0 rm (" + subbedTree[nd] + ") show")
    xx.insert(nd, x)
    x+=20
    yy.insert(nd, 10)

treeThing = re.sub('\(?([A-Z])([A-Z])\)?', '$1', tree)
print treeThing

while (thing3):
    print ("n " + str(xx[1]) + " " + str(yy[1]) + "m")
    if(yy[1] >= yy[2]):
        yy[1] += 20
    print (xx[1] + " " + yy[1] + " l " + xx[2] + " " + yy[1] + " l " + xx[2] + " " + yy[2] + " l s\n")
    xx[1] = 0.5 * (xx[1] + xx[2])
    
