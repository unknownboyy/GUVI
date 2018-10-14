def ispower(n):
    if n&(n-1):
        return True
    return False
n=int(input())
print('yes') if ispower(n) else print('no')