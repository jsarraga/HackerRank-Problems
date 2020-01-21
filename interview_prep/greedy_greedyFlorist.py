#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # the key here is to have each person use their first purchase on the most expensive items. 
    # That's why we sort from expensive to cheap.
    c.sort(reverse=True)
    cost = 0
    previous_purchase = 0

    for i in range(n):
        # formula given: (prev price + 1) * og price
        cost += (previous_purchase + 1) * c[i]
        # checks if we've already cycled through k. aka checks if everyone has made their first purchase
        if (i+1) % k == 0 and (i+1) // k > 0:
            # if everyone has made a purchase, increase previous_purchase by 1
            previous_purchase += 1
    return cost    
    
