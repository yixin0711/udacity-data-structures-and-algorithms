#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:59:00 2020

@author: Sharonvy
"""

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        print("Invalid Data Type")
        return
    
    if number < 0:
        print("Invalid Input, should be positive number")
        return
    
    if number == 0 or number == 1:
        return number
    
    start = 0
    end = number

    return sqrt_recursive(start, end, number)

def sqrt_recursive(start, end, number):
    
    if start <= end:
        
        mid = (start + end)//2
        if mid*mid == number:
            return mid
        elif mid*mid < number:
            if (mid+1)*(mid+1) > number:
                return mid
            else:
                return sqrt_recursive(mid+1, end, number)
        else:
            return sqrt_recursive(start, mid-1, number)
            

#Test edge cases
sqrt(-1)        #should print "Invalid Input, should be positive number"
sqrt('0')       #should print "Invalid Data Type"

#all below test case should print pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")

#Test functionality
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")