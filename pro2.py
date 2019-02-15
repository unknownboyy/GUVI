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