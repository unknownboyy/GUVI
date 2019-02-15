# Distinct Pairs

def numberOfPairs(arr, k):
    # Write your code here
    d = dict()
    for i in arr:
        if i not in d:
            d[i]=1
    count = 0
    if arr.count(k//2)>1:
        count=1
    for i in set(arr):
        if (i in d) and (k-i) in d:
            count+=1
    return count//2
