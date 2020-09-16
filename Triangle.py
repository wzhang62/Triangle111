# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def validinput(a):
    if a > 0:
        return True
    else:
        return 'invalid input'

def validlength(a,b,c):
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'invalid triangle'
    return True




def classifyTriangle(a,b,c):

    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of
    you test cases.

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    if validinput(a) and validinput(b) and validinput(c) and validlength(a,b,c) is True:
        if a == b and b == c:
            return 'equilateral triangle'

        elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            return 'right triangle'

        elif (a != b) and (b != c) and (a != c):
            return 'scalene triangle'

        else:
            return 'isosceles triangle'
    else:
        return 'invalid input'


