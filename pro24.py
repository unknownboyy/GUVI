# Selling Products

import math
import os
import random
import re
import sys



#
# Complete the 'deleteProducts' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ids
#  2. INTEGER m
#

def deleteProducts(ids, m):
    d = dict()
    for i in ids:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    w = list(d.values())
    w.sort()
    count = len(w)
    for i in range(len(w)):
        if m>w[i]:
            m-=w[i]
            count-=1
        elif m==w[i]:
            m=0;count-=1;break
        else:
            break
    return count


if __name__ == '__main__':

    ids_count = int(input().strip())

    ids = []

    for _ in range(ids_count):
        ids_item = int(input().strip())
        ids.append(ids_item)

    m = int(input().strip())

    result = deleteProducts(ids, m)

    print(str(result) + '\n')

