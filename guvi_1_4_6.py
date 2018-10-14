def isspecial(n):
    if n>=48 and n<=57:
        return True
    elif n>=65 and n<=90:
        return True
    elif n>=97 and n<=122:
        return True
    return False
special_count=0
for i in input():
    if isspecial(ord(i)):
        special_count+=1
print(special_count)