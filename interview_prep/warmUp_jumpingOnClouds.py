"""
Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. 
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided. 
For example, c = [0,1,0,0,0,1,0] indexed from 0...6. The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . 
She could follow the following two paths: 0->2->4->6 or 0->2->3->4->6. The first path takes 3 jumps while the second takes 4.

Function Description
Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.
jumpingOnClouds has the following parameter(s):
    c: an array of binary integers

Sample Input 
7
0 0 1 0 0 1 0

Sample Output 
4
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current = 0 #counters to account for current location, and # of jumps
    jumps = 0

    while current < len(c) - 1:  # while we are still within the list length
        if current + 2 < len(c) and c[current + 2] != 1: #if we jump two spots, are we in the list still, and if the number isn't a 1
            current += 1  # then we change our location +1, then + another 1 down below
        current += 1    # if the element two indexes ahead == 1, then increase the current location and jumps by 1
        jumps += 1
    return jumps

    # c = [ 0 0 1 0 0 1 0 ]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()