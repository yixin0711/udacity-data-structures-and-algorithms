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
    
    items = merge(input_list)
    list1 = list()
    list2 = list()
    
    for item in items:
        if len(list1) > len(list2):
            list2.append(str(item))
        else:
            list1.append(str(item))
    
    return [int("".join(list1)), int("".join(list2))]
    

def merge(lst):
    if len(lst) < 2:
        return lst
    
    middle = len(lst)//2
    left = merge(lst[:middle])
    right = merge(lst[middle:])
    
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1
    return lst


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