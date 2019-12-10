"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar = [1,2,1,2,1,3,2]. There is one pair of color 1 and one of color 2. 
There are three odd socks left, one of each color. The number of pairs is 2.

Function Description
Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
    n: the number of socks in the pile
    ar: the colors of each sock

Sample Input
9
10 20 20 10 10 30 50 10 20

Sample Output
3
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    return (sum(ar.count(x)//2 for x in set(ar))) # iterate through the list, count colors and // 2 to pair them up. Then sum it all.

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
