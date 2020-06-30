#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:41:58 2020

@author: Sharonvy
"""

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if not isinstance(input_list, list):
        print("Invalid Data Type")
        return 
    
    if len(input_list) == 0:
        return input_list
    
    start = 0
    mid = 0
    end = len(input_list) - 1
    
    while mid <= end:
        if input_list[mid] == 0:
            temp = input_list[start]
            input_list[start] = input_list[mid]
            input_list[mid] = temp
            start += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            temp = input_list[mid]
            input_list[mid] = input_list[end]
            input_list[end] = temp
            end -= 1
    return input_list




def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

#test edge cases
sort_012('[0, 1, 2]')       #should print "Invalid Data Type"
#all below tests should print pass
print("Pass" if sort_012([]) == [] else "Fail") 
        
#test functionality
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])