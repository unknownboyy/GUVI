# Minimum AMount

import math
import os
import random
import re
import sys


def calculateAmount(prices):
    total_cost = prices[0]
    till_min = prices[0]
    for i in range(1,len(prices)):
        till_min = min(till_min,prices[i])
        total_cost+=(prices[i]-till_min)
    return total_cost

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    result = calculateAmount(prices)

    print(str(result) + '\n')

