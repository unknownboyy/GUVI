n=int(input())
s=list(map(int,input().split()))
su,k=map(int,input().split())
ss=s[:k]
counting=0
if ss==su:
    counting+=1
for i in range(k,n):
    ss+=s[i]
    ss-=s[i-k]
    if ss==su:
        counting+=1
print(counting)