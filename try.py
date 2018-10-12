for _ in range(int(input())) :
    input()
    l=sorted(list(set(list(map(int,input().split()))) & set(list(map(int,input().split()))) & set(list(map(int,input().split())))))
    print(*l) if len(l)>0 else print(-1)
