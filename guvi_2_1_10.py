s1=list(input())
s2=list(input())
flag=2
for i in range(min(len(s1),len(s2))):
    if s1[i]!=s2[i]:
        flag-=1
if abs(len(s1)-len(s2))>=2:
    print('no')
elif flag>0:
    print('yes')
else:
    print('no')