# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:20:32 2014

@author: eocallaghan
"""
#void function check_fermat takes 4 integers 
#answers the question is  a^n + b^2 equal to c^n if n>2
def check_fermat(a, b, c, n):
    leftSideOfEq = a**n + b**n
    rightSideOfEq = c**n
    if (leftSideOfEq==rightSideOfEq & n > 2):
        print "Holy smokes, Fermat was wrong!"
    else:
        print "Nope, doesn't work"

#void function input_fermat takes no values
#uses user input to call check_fermat
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