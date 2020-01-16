#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # make a dictionary of {characters: frequencies}
    char_map = Counter(s)
    # make a dictionary of {character_frequecies: frequencies} i.e: there were 7 times that char's occured 2 times, and once where an e occured 3 times
    char_occurence_map = Counter(char_map.values())
   
   # if everything occured the same amount of times, then TRUE
    if len(char_occurence_map) == 1:
        return "YES"

    theValues = list(char_occurence_map.values())
    theKeys = list(char_occurence_map.keys())
    
    # if there were various frequencies of letters
    if len(char_occurence_map) == 2:
        # if there is only 1 character that occurs more than the others
        # AND there are only one of them (special case in sentence 2)
        if (theKeys[1] - theKeys[0] <= 1) and theValues[1] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
 
    return "NO"
 

    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "abcdefghhgfedecba"

    result = isValid(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
