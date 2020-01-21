#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    # 1. Create a temp array (temp) that stores the position (pos) of elements (val) in the original array (arr) (since they are consecutive)
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    swaps = 0
    

    for i in range(len(arr)):
        # if the correct value isn't in the correct index (if 1 isn't at index[0]) then increase swaps
        if arr[i] != i+1:
            swaps += 1
            # finds value at the current index 
            t = arr[i]
            # assigns correct value in (arr)
            arr[i] = i+1
            # swaps positions with value that was at the index (t)
            arr[temp[i+1]] = t
            # assigns the new pos of element in temp array
            temp[t] = temp[i+1]
    return swaps


arr = [4, 3, 1, 2]
minimumSwaps(arr)
