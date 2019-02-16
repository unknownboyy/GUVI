try:
    number,k_value=map(int,input().split())
    if k_value*2<=number:
        print(1,k_value)
    elif k_value>number:
        print(-1)
    else:
        print(1,number-k_value)
except:
    print('Invalid Input')