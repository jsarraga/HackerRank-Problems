""" 

Day 2 operators

Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!

Sample Input
12.00
20
8

Sample Output
15
"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost * (tip_percent / 100))
    tax = float(meal_cost * (tax_percent / 100))
    totalcost = float(meal_cost + tip + tax)
    print(round(totalcost))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)