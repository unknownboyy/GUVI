try:
    alpha,beta,fafa,kuku=map(int,input().split())
    if beta>=2*alpha:
        print(kuku//2)
    elif beta>2*alpha-fafa:
        print(kuku-1)
    elif beta>=alpha:
        print(kuku)
    else:
        print(-1)
except:
    print('Invalid Input')