# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:15:21 2021

@author: Admin
"""

import sys
infile = sys.argv[1]
outfile = sys.argv[2]
f1 = open(infile,'r')
f2 = open(outfile,'w')
for line in f1:
    line =line.strip("\n")
    a = len(line)
    f2.write(str(a)+"\n")
f1.close()
f2.close()
    
    