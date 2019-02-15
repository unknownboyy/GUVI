#!/bin/python3

import math
import os
import random
import re
import sys


def findBreakDuration(n, k, t, start, finish):
    s = []
    for i in range(n):
        s.append([start[i],finish[i]])
    s = sorted(s,key=lambda x:(x[1],x[0]))
    w = s.copy()
    max_time = 0
    for i in range(n-k+1):
        s = w.copy()
        for j in range(i,i+k):
            if j==0:
                shift = s[j][0]
                s[j][0]-=shift
                s[j][1]-=shift
            else:
                shift = s[j-1][1]-s[j][0]
                s[j][0]-=shift
                s[j][1]-=shift
        if i+k==n:
            max_time = max(max_time,n-s[i+k-1][1])
        else:
            max_time = max(max_time,s[i+k][0]-s[i+k-1][1])
        print(s)
    return max_time

if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())

    t = int(input().strip())

    start_count = int(input().strip())

    start = list(map(int,input().split()))

    finish =  list(map(int,input().split()))


    result = findBreakDuration(n, k, t, start, finish)
    print(result)