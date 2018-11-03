def getcost(n):
    left=False
    if n[0]=='d' or n[0]=='f':
        left=True
    tcost=0
    for i in n:
        if i=='d' or i=='f':
            if left:
                tcost+=2
            else:
                left=True
                tcost+=4
        else:
            if not left:
                tcost+=2
            else:
                left=False
                tcost+=4
    return tcost
for _ in range(int(input())):
    times=int(input())
    cost=0
    d=dict()
    appeared=dict()
    for i in range(times):
        word=input()
        if word in d:
            if word not in appeared: d[word]//=2;appeared[word]=1
            cost+=d[word]
        else:
            d[word]=getcost(word)
            cost+=d[word]
    print((cost))