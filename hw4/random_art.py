# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
import random
import Image
import math

def avg(a,b):
    return (a+b)/2


def build_random_function(min_depth, max_depth):
    # your doc string goes here
 
    # xyList = [['x'],['y']]
    
    if (max_depth <= 1): #Random choice might work a little cleaner here
         return random.choice([["x"],["y"]])

    f = build_random_function(min_depth-1, max_depth-1)
    g = build_random_function(min_depth-1, max_depth-1)
    
    prod = ['prod', f, g]
    cos_pi = ['cos_pi', f]
    sin_pi = ['sin_pi', f]
    cubic = ['cubic', f]
    square = ['square',f]
    avg = ['avg',f,g]
    x = ['x']
    y = ['y']
    
    functionList = [prod, cos_pi, sin_p, cubic, square, avg, x, y]
    if (min_depth > 1):
        return functionList[random.randint(0,5)]
    return functionList[random.randint(0,7)]

def evaluate_random_function(f, x, y):
    """ "x" and "y" are the base cases and return either x or y respectively
        this function works by taking a list of functions and x and y value. The function
        then checks what the outermost funtion is and evaluates it for the deeper level functions.
    """
    if (f[0] == "x"):
        return x
    if (f[0] == "y"):
        return y
    if (f[0] == "prod"):
        return evaluate_random_function(f[1],x,y) * evaluate_random_function(f[2],x,y)
    if (f[0] == "cos_pi"):
        return math.cos(math.pi * evaluate_random_function(f[1],x,y))
    if (f[0] == "sin_pi"):
        return math.sin(math.pi * evaluate_random_function(f[1],x,y))
    if (f[0] == "cubic"):
        return (evaluate_random_function(f[1],x,y))**3
    if (f[0] == "square"):
        return (evaluate_random_function(f[1],x,y))
    if (f[0] == "avg"):
        return avg(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
    """
    return (val-input_interval_start)/(input_interval_end - input_interval_start)*(output_interval_end - output_interval_start) + output_interval_start

def draw(x, y, minDepth, maxDepth, number):
    """ Draw creates a new image canvas. It then creates a series of random functions
        for the red green and blue. Then it takes the pixel number and remaps it across
        the interval [-1,1] and evaluates the red blue and green functions with this remapped
        value and then remaps the output to RGB values (the interval [0, 255])
        
    """
    x = int(x)
    y = int(y)
    red = build_random_function(minDepth, maxDepth)
    blue = build_random_function(minDepth, maxDepth)
    green = build_random_function(minDepth, maxDepth)
    im = Image.new("RGB",(x,y))
    for i in range(x):
        for j in range(y):
            imap = remap_interval(i, 0.0, float(x), -1.0,1.0)
            jmap = remap_interval(j, 0.0, float(y), -1.0,1.0)
            redOutput = evaluate_random_function(red, imap, jmap)
            blueOutput = evaluate_random_function(blue, imap, jmap)
            greenOutput = evaluate_random_function(green, imap, jmap)
            redOutput = remap_interval(redOutput, -1.0, 1.0, 0.0, 255.0)
            greenOutput = remap_interval(greenOutput, -1.0, 1.0, 0.0, 255.0)
            blueOutput = remap_interval(blueOutput, -1.0, 1.0, 0, 255.0)
            im.putpixel((i,j),(int(redOutput),int(greenOutput),int(blueOutput)))
    im.save("image" + str(number) + ".bmp")

#Thank you for not running anything outside the functions
#Though, if you want to test your code, put it in a main conditional


if __name__ == "__main__":
    num_pictures = 10
    for i in xrange(num_pictures):
        draw(500,500, 5, 6, i)