#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:19:21 2020

@author: Sharonvy
"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    
    if not isinstance(input_list, list) or not isinstance(number, int):
        print("Invalid Data Type")
        return -1
    
    if len(input_list) == 0:
        print("Empty List")
        return -1
    
    start = 0
    end = len(input_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if number == input_list[mid]:
            return mid
        
        if input_list[start] <= input_list[mid]:
            if input_list[start] <= number <= input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if input_list[mid] <= number <= input_list[end]:
                start = mid +1
            else:
                end = mid - 1
    return -1

def linear_search(input_list, number):
    if not isinstance(input_list, list) or not isinstance(number, int):
        return -1
    
    if len(input_list) == 0:
        return -1
    
    for index, element in enumerate(input_list):
        if element == number:
            return index
    
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print('Pass')
    else:
        print("Fail")

#test edge cases
test_function([[], 0])   #should print "Empty List" and pass
test_function([0,0])    #should print "Invalid Data Type" and pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], None])     #should print "Invalid Data Type" and pass
        
#test functionality
#all test case should print pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])