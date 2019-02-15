# Lottery Coupons

import math
import os
import random
import re
import sys



def lotteryCoupons(n):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = lotteryCoupons(n)

    fptr.write(str(result) + '\n')

    fptr.close()
