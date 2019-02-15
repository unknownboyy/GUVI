# Lottery Coupons
from collections import Counter
def su(n):
    count = 0
    for i in str(n):
        count+=int(i)
    return count

def lotteryCoupons(n):
    mylist = []
    for i in range(1,n+1):
        mylist.append(su(i))
    w = list(Counter(mylist).values())
    return w.count(max(w))