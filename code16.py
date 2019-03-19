for _ in range(int(input())):
    n = int(input())
    x = int((2*n)**0.5)
    if x*(x+1)//2==n:
        print('Go On Bob',x)
    else:
        print('Better Luck Next Time')