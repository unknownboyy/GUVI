t = int(input())
for _ in range(t):
    n,b=map(int,input().split())
    area = -1
    for i in range(n):
        x,y,z=map(int,input().split())
        if z<=b:
            area = max(area,x*y)
    print(area) if area!=-1 else print('no tablet')