# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:20:57 2014

@author: eocallaghan
"""
#void function compare takes two integers
#returns values based on the relationship between x&y
def compare(x,y):
    if (x<y):
        return 1
    elif (x==y):
        return 0
    elif (x>y):
        return -1


print compare(2,5)
print compare(1,1)
print compare(7,4)