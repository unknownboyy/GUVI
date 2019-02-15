#!/bin/python3

import math
import os
import random
import re
import sys



# def powerJump(game):
#     s = game
#     i=0
#     maxi = 0
#     while i<len(s) and s[i]=='0':
#         i+=1
#     maxi=i
#     while i<len(s):
#         left = i
#         right = left+1
#         while right<len(s) and s[right]=='0':
#             right+=1
#         maxi = max(right-left,maxi)
#         i = right
#     i=0
#     maxj = 0
#     while i<len(s) and s[i]=='1':
#         i+=1
#     maxj=i
#     while i<len(s):
#         left = i
#         right = left+1
#         while right<len(s) and s[right]=='1':
#             right+=1
#         maxj = max(right-left,maxj)
#         i=right
#     #print(maxi,maxj)
#     return (min(maxi,maxj))

def powerJump(game):
    maxi = 0
    c = game[0]
    i = 0;init=0
    while i<len(game):
        while i<len(game) and game[i]==c:
            i+=1
        maxi=max(maxi,i-init)
        init=i
        c = game[i] if i<len(game) else None
    return maxi
if __name__ == '__main__':
    game = input()

    result = powerJump(game)

    print(str(result) + '\n')

