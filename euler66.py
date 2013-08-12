# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:26:41 2012

@author: fortran
"""
from euler import solve_diophantine

def not_perfect_square(n):
    int_sq = int(n**0.5)
    return int_sq * int_sq != n

max_d = max(filter(not_perfect_square, xrange(1001)),
            key=solve_diophantine)

print(max_d)