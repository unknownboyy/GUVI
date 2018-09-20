def isprime(n):
    for i in range(2,int(n**0.5)+2):
        if n%i==0:  return False
    return True
t=int(input())
for _ in range(t) :
    n=int(input())
    if isprime(n):  print('Prime')
    else:   print('Not prime')