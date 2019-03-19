# Chef got Recipes
def func(s):
    count = 0
    for i in s:
        if i=='a':
            count|=1
        elif i=='e':
            count|=2
        elif i=='i':
            count|=4
        elif i=='o':
            count|=8
        elif i=='u':
            count|=16
    return count
for _ in range(int(input())):
    n = int(input())
    l = [0]*32
    for i in range(n):
        s = set(input())
        l[func(s)]+=1
    mycount = 0
    for i in range(1<<5):
        for j in range(i,1<<5):
            if i|j==31:
                if i==j:
                    mycount+=(l[i]*(l[j]-1))//2
                else:
                    mycount+=l[i]*l[j]
    print(mycount)