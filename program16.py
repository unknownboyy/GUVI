def getDigit(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count
def oddSum(n):
    su=0
    while n>0:
        su+=n%10
        n//=100
    return su
def evenSum(n):
    su=0
    n//=10
    while n>0:
        tr=(n%10)*2
        su+=(tr%10+tr//10)
        n//=100
    return su
def isModTen(n):
    if n%10==0: return True
    return False
def isPrefix(n,s):
    prefixLength=getDigit(s)
    numberLength=getDigit(n)
    for i in range(numberLength-prefixLength):
        n//=10
    if n==s:    return True
    else:   return False    
def isValid(n):
    if getDigit(n)>=13 and getDigit(n)<=16 and isModTen(oddSum(n)+evenSum(n)) and (isPrefix(n,4) or isPrefix(n,5) or isPrefix(n,6) or isPrefix(n,37)):
        return True
    else:   return False

n=int(input("Enter Card Number"))
if(isValid(n)):
    print('Valid')
else:
    print('InValid')