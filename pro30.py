from math import log
#Factor of 3 and 5

import math
import os
import random
import re
import sys




def getIdealNums(l, r):
    left = log(l,3)
    right = log(r,3)
    count = 0
    for i in range(left,right+1):
        for j in range(left,right+1):
            w =  (3**i)*(5**j)
            if w>=l and w<=r:
                count+=1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    r = int(input().strip())

    result = getIdealNums(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()
