# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 02:19:06 2014

@author: eocallaghan
"""

#defines the characters to be used in the box
dash = "- "
plus = "+ "
space = " "
verticalLine = "|"
#defines the line with the dashes
row = plus + dash*4 + plus + dash*4 + plus
#defines the line with the vertical lines
column = verticalLine + space*9 + verticalLine + space*9 +verticalLine
#repeatly prints the row and column lines... because loops don't exist
print row
print column
print column
print column
print column
print row
print column
print column
print column
print column
print row