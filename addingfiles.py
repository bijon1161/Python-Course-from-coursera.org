# -*- coding: utf-8 -*-
"""
Created on Mon May 17 18:49:34 2021

@author: Admin
"""

def addfile(file1,file2):
    infile1=open(file1,"r")
    infile2=open(file2,"r")
    for line in infile1:
        num1_ = int(line)
    for line in infile2:
        num2_ = int(line)
    print(num1_+num2_)
    infile1.close()
    infile2.close()