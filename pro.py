# Dragon and Bangeon

import math
import os
import random
import re
import sys



#
# Complete the 'minHealth' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY dungeon as parameter.
#

def minHealth(dungeon):
    w = 0
    m = 1000000
    for i in range(len(dungeon)):
        w+=dungeon[i]
        m = min(m,w)
    return -m+1

if __name__ == '__main__':

    dungeon_count = int(input().strip())

    dungeon = []

    for _ in range(dungeon_count):
        dungeon_item = int(input().strip())
        dungeon.append(dungeon_item)

    result = minHealth(dungeon)

    print(str(result) + '\n')