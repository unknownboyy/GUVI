for _ in range(int(input())) :
    s=input()
    su=0;totals=0
    for i in range(len(s)):
        x=ord(s[i])
        if x>=48 and x<=57:
            su=su*10+x-48
        else:
            totals=totals+su
            su=0
    print(totals+su)