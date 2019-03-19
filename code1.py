for _ in range(int(input())):
    n,k = map(int,input().split())
    s = list(map(int,input().split()))
    flag=False
    l = [0]
    for i in range(n-1):
      if s[i]<=s[i+1]:
        pass
      else:
        l.append(i)
    for i in l:
        penalty = 0
        for j in range(i,n):
            penalty+=int(s[j]/(j-i+1))
        if penalty<=k:
            flag=True
            break
    if flag:
        print(i+1)
    else:
        print(n+1)