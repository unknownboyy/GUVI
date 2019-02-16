#!/bin/python3

import math
import os
import random
import re
import sys

def leftshift(s,times):
    pass
def rightshift():
    pass


def findBreakDuration(n, k, t, start, finish):
    s = [[0,0]]
    for i in range(n):
        s.append([start[i],finish[i]])
    s = sorted(s,key=lambda x:(x[1],x[0]))
    while s[-1][1]>t:
        s.pop()
    s.append([t,t])
    max_time = 0
    for i in range(n-1):
        rightshift(s)

if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    t = int(input().strip())

    start_count = int(input().strip())

    start = list(map(int,input().split()))

    finish =  list(map(int,input().split()))


    result = findBreakDuration(n, k, t, start, finish)
    print(result)