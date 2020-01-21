#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    # sort in decreasing order
    contests.sort(reverse=True)
    luck = 0

    for contest in contests:
        # we can lose as many uninmportant contests as we want and increase associated luck
        # if it's unimportant (0), then we'll lose it and increase the associated luck
        if contest[1] == 0:
            luck += contest[0]
        # if we have important contests left to lose
        # let's lose them and increase associated luck
        # and decrease k by 1
        elif k > 0:
            luck += contest[0]
            k -= 1
        # otherwise, we'll win the contest and decrease the luck from our count
        else:
            luck -= contest [0]
    return luck

# Since it's in descending order, the more valuable, 
# higher luck elements will be considered before the lesser ones


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
