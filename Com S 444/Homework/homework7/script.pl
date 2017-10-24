#!/usr/bin/perl
#drawtree.pl -- draws binary trees (root at top}
#usage : echo '(A((BC)D)(EF))' drawtree.pl > output.ps
#from Arthur Lesk 2014
print <<EOF;
%!PS-Adobe-
%%BoundingBox : atend
/n /newpath load def
/m /moveto load def
/l /lineto load def
/rm /rmoveto load def
/rl /rlineto load def
/s /stroke load def
1.0 setlinewidth 50 100 translate 2 2 scale
/Helvetica findfont 10 scalefont setfont
EOF
$tree = <>; chop($tree); $_= reverse($tree); s/[()]//g;
$x = 0; $y = 0;
while ($nd = chop()) {
print "$x $y m ($nd) stringwidth pop -0.5 mul 0 rm ($nd) show\n";
$xx{$nd} = $x; $x+=20 ; $yy{$nd} = 10;
}
while ($tree =~ s/\(?([A-Z])([A-Z])\)?/$1/){
print "n $xx{$1} $yy{$1} $1 $2 $xx{$2} $yy{$2} m\n";
($yy{$1} > $yy{$2}) || {$yy{$1} = $yy{$2}}; $yy{$1} += 20;
print "$xx{$1} $yy{$1} l $xx{$2} $yy{$1} l $xx{$2} $yy{$2} l s\n";
$xx{$1} = 0.5*($xx{$1} + $xx{$2});
}
print "n $xx{$tree} $yy{$tree} m 0 20 rl s showpage\n";
$rx = 2*$x + 30; $yt = 2*$yy{$tree} + 146;
print "%%BoundingBox : 40 95 $rx $yt\n" ;