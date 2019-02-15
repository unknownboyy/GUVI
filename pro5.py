for _ in range(int(input())):
    n = int(input());s = set(input())
    for i in range(n-1):    s = s & set(input())
    print(len(s))