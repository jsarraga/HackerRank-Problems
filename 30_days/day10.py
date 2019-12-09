"""
Day 10 : Binary Numbers

Task
Given a base- integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in 's binary representation.

Input Format

A single integer, n.

Constraints
1 <= n <= 10^6

Output Format
Print a single base- integer denoting the maximum number of consecutive 's in the binary representation of .

Sample Input 1
5

Sample Output 1
1

Sample Input 2
13

Sample Output 2
2

Sample Case 1:
The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13 is 1101, so the maximum number of consecutive 1's is 2.
"""



#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input())

    #counters
    current_consecutive = 0
    max_consecutive= 0
    
    #The key here is to find out the formula to convert an integer into a binary number
    while n > 0:
        remainder = n % 2
        if remainder == 1: 
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive 
        else:
            current_consecutive = 0
        n = n // 2 

    print(max_consecutive)