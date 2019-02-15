<<<<<<< HEAD
# Custom Sort
# Can You Sort?

import math
import os
import random
import re
import sys
from collections import Counter


def customSort(arr):
    w = Counter(arr)
    left = list(w.values())
    right = list(w.keys())
    middle = zip(right,left)
    middle = sorted(middle,key=lambda x:(x[1],x[0]))
    w = []
    for i in middle:
            w+=[i[0]]*i[1]
    print(*w,sep='\n')

if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    customSort(arr)
=======
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if len(a)!=len(b):
        print('Alice')
    else:
        print('Bob')
>>>>>>> 33f4cd762d4e4b8b825025741676af85251a142b
