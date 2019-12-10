"""
Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s='abcac' and n=10, the substring we consider is abcacabcac, the first 10 characters of her infinite string. 
There are 4 occurrences of a in the substring.

Function Description
Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length n in the infinitely repeating string.

repeatedString has the following parameter(s):
    s: a string to repeat
    n: the number of characters to consider

Sample Input 
aba
10

Sample Output 
7

Explanation 0
The first n=10 letters of the infinite string are abaabaabaa. Because there are 7 a's, we print 7 on a new line.

Sample Input 
a
1000000000000

Sample Output 
1000000000000

Explanation 1
Because all of the first n=1000000000000 letters of the infinite string are a, we print 1000000000000 on a new line.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count_string = s.count('a') # counts the number of "a" in a full string,
    a_count_substring = s[0:n%len(s)].count('a') #calculates the total amount of "a" based on the potentially partial string
    return a_count_string * (n//len(s)) + a_count_substring ##"a" count of full string * number of string repeats + "a" count of last string.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()