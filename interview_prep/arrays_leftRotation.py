"""
A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1,2,3,4,5], then the array would become [3,4,5,1,2].

Given an array a of n integers and a number, d, perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

    An array of integers a.
    An integer d, the number of rotations.

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(0,d):  # loop through array
        first = a.pop(i)  #  pop the first element of the list
        a.append(first)   # append it to the end of the list
    return(a)

# MORE EFFICIENT WAY
def rotLeft(a, d):
    return a[d:] + a[:d]  # splice the list at index d, take second half and add it to the first half
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()






