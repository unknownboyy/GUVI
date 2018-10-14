term,start,common_diff=map(int,input().split())
su=start
for i in range(1,term):
    su=su+(i+1)*common_diff
print(su)