#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    min_edge = min(a, b, c)
    a1, b2, c3 = sorted([a, b, c])    

    if min_edge <= 0 or a1 + b2 <= c3:
        raise TriangleError

    sides = set([a, b, c])

    if len(sides) == 1: return "equilateral"
    elif len(sides) == 2: return "isosceles"
    elif len(sides) == 3: return "scalene"
    



    


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    # if negative number
    # c – b < a < c + b
    # if zero
    #or


    pass
