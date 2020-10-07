# -*- coding: utf-8 -*-


import unittest

from Triangle import classifyTriangle


class TestTriangles(unittest.TestCase):
    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(2,3,0),'invalid input')

        self.assertEqual(classifyTriangle(-2,3,5),'invalid input')

    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(6,3,2),'invalid input')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'right triangle','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'right triangle','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'equilateral triangle','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3,2,3),'isosceles triangle','3,2,3 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(5,11,12),'scalene triangle','5,11,12 should be scalene' )

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

