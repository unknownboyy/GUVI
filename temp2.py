from time import time

# Recursion
def fibo1(n):
    if n<=1:
        return n
    return fibo1(n-2)+fibo1(n-1)
n = 33
f = [-1]*(n+1)
call = 0

# Memoization
def fibo2(n):
    if f[n]==-1:
        if n<=1:    return n
        else:   f[n]=fibo2(n-2)+fibo2(n-1)
    return f[n]

# Tabulation
def fibo3(n):
    ff = [0,1]
    for i in range(2,n+1):
        ff.append(ff[-1]+ff[-2])
    return ff[n]

start = time()
fibo1(n)
lap1 = time()
fibo2(n)
lap2 = time()
fibo3(n)
end = time()

print('Time in Recursion',lap1-start)
print('Time in Memoization',lap2-lap1)
print('Time in Tabulation',end-lap2)