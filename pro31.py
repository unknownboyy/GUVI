#!/bin/python3

import math
import os
import random
import re
import sys
from math import ceil
def getpos(s,ele):
    pos = len(s)
    while s[-1]>ele:
        pos-=1
    return pos
def myarry(s,k):
    s.sort()
    while k>0:
        s.append(ceil(s.pop()/2))
        s.sort()
        k-=1
    return sum(s)

def minSum(num, k):
    return myarry(num,k)

if __name__ == '__main__':
    num_count = int(input().strip())

    num = []

    for _ in range(num_count):
        num_item = int(input().strip())
        num.append(num_item)

    k = int(input().strip())

    result = minSum(num, k)

    print(str(result) + '\n')

