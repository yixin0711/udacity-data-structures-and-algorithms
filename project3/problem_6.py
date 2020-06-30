#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:59:51 2020

@author: Sharonvy
"""

import random

def get_min_max(ints):
    
    n = len(ints)
    if not isinstance(ints, list):
        print("Invalid input data type")
        return None
    
    if n == 0:
        print("Empty list")
        return None
    
    if n == 1:
        max_int = ints[0]
        min_int = ints[0]
        return (min_int, max_int)

    if ints[0] > ints[1]:
        max_int = ints[0]
        min_int = ints[1]
    else:
        max_int = ints[1]
        min_int = ints[0]
        
    for i in range(2, n):
        if ints[i] > max_int:
            max_int = ints[i]
        elif ints[i] < min_int:
            min_int = ints[i]
    
    return (min_int, max_int)

#test edge cases
test1 = ""
test2 = []
print("Pass" if None == get_min_max(test1) else "Fail")    # should print "Invalid input data type" and pass
print("Pass" if None == get_min_max(test2) else "Fail")    # should print "Empty list" and pass

#test functionality
l = [i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if (0,9) == get_min_max(l) else "Fail")       # should print pass