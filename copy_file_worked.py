# -*- coding: utf-8 -*-


""" Opens two files and copies one into the other line by line. """
import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename,'w')

for line in infile:
    outfile.write(line)
    
infile.close()
outfile.close()