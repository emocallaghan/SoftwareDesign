# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:20:32 2014

@author: eocallaghan
"""

def check_fermat(a, b, c, n):
    leftSideOfEq = a**n + b**n
    rightSideOfEq = c**n
    if (leftSideOfEq==rightSideOfEq & n!= 2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "Nope, doesn't work"

def input_fermat():
    a = raw_input("Please enter the number for a: ")
    b = raw_input("Please enter the number for b: ")
    c = raw_input("Please enter the number for c: ")
    n = raw_input("Please enter the number for n: ")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_fermat(a,b,c,n)

input_fermat()