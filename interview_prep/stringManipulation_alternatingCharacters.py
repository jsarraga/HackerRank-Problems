#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    counter = 0 # start a counter 
    for i in range(len(s)-1):  # iterate through the characters in the string 
        if s[i] == s[i+1]:     # to find out if a character is the same as it's neighbor 
            counter += 1       # if it is, then increase the counter by 1
    return counter 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
