# Separate Students

import math
import os
import random
import re
import sys

def left(avg):
    moves = 0
    i = 0
    j = len(avg)-1
    while i<j:
        while i<len(avg) and avg[i]==1:
            i+=1
        while j>=0 and avg[j]==0:
            j-=1
        if i<j:
            moves+=(j-i)
            i+=1;j-=1
        else:
            break
    return moves


def minMoves(avg):
    return min(left(avg[::]),left(avg[::-1]))

if __name__ == '__main__':
    avg_count = int(input().strip())

    avg = list(map(int,input().split()))

    result = minMoves(avg)

    print(str(result) + '\n')
