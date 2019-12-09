"""
Day 11: 2d Arrays aka Matrix
Hourglass problem

Context
Given a 6x6 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
a b c
  d
e f g

There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Input Format

There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A; every value in A will be in the inclusive range of -9 to 9.

Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output
19
"""

#The key is to use the middle number of the hourglass as a starting point. 
#Row[0] and Row[n-1] are the edge cases - they cannot be the center of an hourglass
#use two-nested for loops:
#   loop over all rows in outer for loop, then loop over each column for each row in the inner for loop

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    def _get_hourglass_sum(matrix, row, col):
        sum = 0
        sum += matrix[row-1][col-1]  #sums all positions of hourglass in relation to center
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]
        sum += matrix[row][col]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]
        return sum

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_hourglass_sum = -63 # minimal hourglass sum possible 9 * -9
    for i in range(1,5): # dont need to iterate through first/last rows or columns bc they can't be the center of an hourglass
        for j in range(1,5): 
            current_hourglass_sum = _get_hourglass_sum(arr, i,j)
            if current_hourglass_sum > max_hourglass_sum:  #if current hourglass is larger than max, it becomes new max
                max_hourglass_sum = current_hourglass_sum

    print(max_hourglass_sum)