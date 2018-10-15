from math import ceil,floor
n,m=map(int,input().split())
number=(n*m)**0.5
if ceil(number)==float(number):
    print('yes')
else:
    print('no')