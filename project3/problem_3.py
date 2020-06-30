#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 16:17:07 2020

@author: Sharonvy
"""

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    if not isinstance(input_list, list):
        print("Invalid input data type")
        return None
    
    if len(input_list) == 0:
        print("Empty list")
        return None
    
    if len(input_list) == 1:
        return input_list
    
    items = reverse_mergesort(input_list)
    list1 = list()
    list2 = list()
    
    for item in items:
        if len(list1) > len(list2):
            list2.append(str(item))
        else:
            list1.append(str(item))
    
    return [int("".join(list1)), int("".join(list2))]
    

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    
    merged += left[left_index:]
    merged += right[right_index:]
    
    return merged
    
def reverse_mergesort(ints):
    if len(ints) <= 1:
        return ints
    
    index = len(ints) // 2
    left = ints[:index]
    right = ints[index:]
    
    left = reverse_mergesort(left)
    right = reverse_mergesort(right)
    
    return merge(left, right)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

#test edge cases
rearrange_digits([])        #should print "Empty list"
rearrange_digits('3, 4, 5, 6, 7') #should print "Invalid input data type"

#test functionality
test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2 = [[2, 1], [2, 1]]
test_case3 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case1)       #should print pass
test_function(test_case2)       #should print pass
test_function(test_case3)       #should print pass