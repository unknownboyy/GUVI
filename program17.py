def setDigit(n):
    return n*10**(16-getDigit(n))
def setPrefix(n):
    su=0;i=0
    while n>9:
        su+=(n%10)*10**i
        n//=10
        i+=1
    return 4*10**i+su
def setMod(n):
    su=oddSum(n)+evenSum(n)
    ll=list(str(n))[::-1]
    for i in range(len(ll)):
        if i%2==0:
            if int(ll[i])>su:
                ll[i]=chr(ord(ll[i])-su)
                return int("".join(ll))

    
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
def isValid(n):
    if getDigit(n)>=13 and getDigit(n)<=16 and isModTen(oddSum(n)+evenSum(n)) and (isPrefix(n,4) or isPrefix(n,5) or isPrefix(n,6) or isPrefix(n,37)):
        return True
    else:   return False
def makeValid(n):
    if getDigit(n)>=13 and getDigit(n)<=16: pass
    else:   n=setDigit(n)
    if isPrefix(n,4) or isPrefix(n,5) or isPrefix(n,6) or isPrefix(n,37):   pass
    else:   n=setPrefix(n)
    if isModTen(n): pass
    else:   n=setMod(n)
    print(n)
    if isValid(n):  return n
    else:   return -1
n=int(input("Enter Card Number from whwre you want to start"))
"""
if(isValid(n)):
    print('Valid')
else:
    print('InValid')
    """
print(makeValid(n))