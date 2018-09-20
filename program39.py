from math import *
for _ in range(int(input())) :
    m,n=map(int,input().split())
    x=int(log(m,n))
    print(n**x)