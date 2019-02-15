

import math
import os
import random
import re
import sys


my_list = []
def summy(s,mm):
    ss = 0
    for i in range(7):
        ss+=int(s[i])
    if ss==mm:
        return True
    else:
        return False
def func(i,s,max_day,till_sum,mm):
    if i>=7:
        if mm==till_sum and summy(s,mm):    my_list.append(s[:7])
    else:
        while i<7 and s[i]!='?':
            i+=1
        for j in range(max_day+1):
            func(i+1,s[:i]+str(j)+s[i+1:],max_day,till_sum+j,mm)


def findSchedules(workHours, dayHours, pattern):
    n = workHours
    max_day = dayHours
    s = pattern
    till_sum = 0
    for i in s:
        if i!='?':
            till_sum+=int(i)
    i = 0
    while i<7 and s[i]!='?':
        i+=1
    func(i,s,max_day,till_sum,n)
    return my_list

if __name__ == '__main__':

    workHours = int(input().strip())

    dayHours = int(input().strip())

    pattern = input()

    result = findSchedules(workHours, dayHours, pattern)

    print('\n'.join(result))
