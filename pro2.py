for _ in range(int(input())) :
    n=int(input())
    times=n//26+1
    mod=n%26
    if mod<=2:
        print(times,0,0)
    elif mod<=10:
        print(0,times,0)
    else:
        print(0,0,times)