<<<<<<< HEAD
# 0/1 waala
s = input()
one = s.count('1')
zero = s.count('0')
x=int(input())
y=int(input())
w = min(zero//x,one//y)
print(('0'*x+'1'*y)*w,end='')
one-=w*y
zero-=(w*x)
print('0'*zero+'1'*one)
=======
for i in range(int(input())):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    count=0
    for i in s:
        if i!=1:
            count+=1
    if count<=k:
        print('YES')
    else:
        print('NO') 
>>>>>>> 33f4cd762d4e4b8b825025741676af85251a142b
