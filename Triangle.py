# -*- coding: utf-8 -*-


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


