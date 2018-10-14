factors=0
n=int(input())
for i in range(2,n):
    if n%i==0:
        factors+=1
print('no') if factors>0 else print('yes')