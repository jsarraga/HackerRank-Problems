#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):\
    # could use a nested loop to compare all elements to each other --> O(n^2)
    # sorting in ascending order --> O(nlog(n))

    arr.sort() # sort in ascending order
    min_diff = inf
    for i in range(len(arr)-1): # loop through arr
        diff = abs(arr[i] - arr[i+1]) # compare each element
        if diff < min_diff:  # if diff is smaller than prev min_diff
            min_diff = diff  # set new min_ diff to diff
    return min_diff

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
