n = int(input())
s = list(map(int,input().split()))
x = 0
for i in s:
    x^=i
flag = False
for i in s:
    if x^i in s:
        flag=True
if ((x==0 or (x not in s)) and flag==True) or (flag==False and n>3):
    print('Alice')
else:
    print('Bob')
