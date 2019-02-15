#!/bin/python3

import math
import os
import random
import re
import sys

myarr=['a','e','i','o','u']

def find(s):
    arr = [[0 for i in range(5) for i in range(len(s))]
    for i in range(len(s)-1,-1,-1):
        if i<len(s)-1:
            s[i][0]=s[i+1][0]
            s[i][1]=s[i+1][1]
            s[i][2]=s[i+1][2]
            s[i][3]=s[i+1][3]
            s[i][4]=s[i+1][4]
        if s[i]=='u':
            s[i][4]+=1


def longestSubsequence(s):
    return None

if __name__ == '__main__':
    s = input()
    result = longestSubsequence(s)
    print(str(result) + '\n')