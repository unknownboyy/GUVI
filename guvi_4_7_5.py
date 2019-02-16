try:
    n,k=map(int,input().split())
    s = list(map(int,input().split()))
    w = (sum(s)-s[k])//2
    charge = int(input())
    if charge==w:
        print('Bon Appetit')
    else:
        print(charge-w)
except:
    print('Invalid Input')