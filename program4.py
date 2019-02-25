from math import log,ceil
for _ in range(int(input())):
    n = int(input())
    d2 = ceil(log(n,2))
    i = 1
    while n*i>=(2**(i)-1):
        i+=1
    print(i-1,d2)