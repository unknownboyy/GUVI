# Good Segment

import math
import os
import random
import re
import sys



def goodSegment(badNumbers, l, r):
    badNumbers.sort()
    count = 0
    while badNumbers[0]<l:
        badNumbers.pop(0)
    while badNumbers[-1]>r:
        badNumbers.pop()
    badNumbers.insert(0,l)
    badNumbers.append(r)
    print(*badNumbers)
    for i in range(1,len(badNumbers)):
        if badNumbers[i-1]+1<badNumbers[i]:
            if i==len(badNumbers)-1:
                count  = max(count,badNumbers[i]-badNumbers[i-1])
            else:
                count  = max(count,badNumbers[i]-badNumbers[i-1]-1)
    return count

if __name__ == '__main__':

    badNumbers_count = int(input().strip())

    badNumbers = []

    for _ in range(badNumbers_count):
        badNumbers_item = int(input().strip())
        badNumbers.append(badNumbers_item)

    l = int(input().strip())

    r = int(input().strip())

    result = goodSegment(badNumbers, l, r)

    print(str(result) + '\n')
