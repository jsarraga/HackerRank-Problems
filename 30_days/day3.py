"""

Day 3: Intro to Conditional Statements

Objective
In this challenge, we're getting started with conditional statements. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.


Sample Input 0
3

Sample Output 0
Weird

Sample Input 1
24

Sample Output 1
Not Weird
"""


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
if N % 2 != 0:
    print("Weird")
elif N % 2 == 0 and N >= 2 and N <= 5:
    print("Not Weird")
elif (N % 2 == 0) and (N >= 6) and (N <= 20):
    print("Weird")
elif (N % 2 == 0) and N > 20:
    print("Not Weird")