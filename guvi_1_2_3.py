def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
print('yes') if isprime(n) else print('no')