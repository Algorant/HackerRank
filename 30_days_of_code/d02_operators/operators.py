#Python 3 Solution

import math
import os
import random
import re
import sys

# Basic function to calculate tip, tax, and total cost

def solve(meal_cost, tip_percent, tax_percent):

    total_tip = (meal_cost * tip_percent) / 100

    total_tax = (meal_cost * tax_percent) / 100

    total_cost = round(round(meal_cost + total_tip + total_tax))

    print(total_cost)

# Takes inputs for meal cost, the tip %, and the tax %, then solves

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
