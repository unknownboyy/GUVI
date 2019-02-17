from math import log
try:
    t = int(input())
    r = int(log((t-1)/3+1)/log(2))+1
    print(3*2**r-t-2)
except:
    print('Invalid Input')