try:
    n = int(input())
    if n==1:
        print(2)
        print(1,1)
    else:
        print(2*n-1)
        print(n,end=' ')
        for i in range(n,1,-1):
            print(i-1,i,end=' ')
except:
    print('Invalid Input')