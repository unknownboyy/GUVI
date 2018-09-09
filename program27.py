vowel=['a','e','i','o','u','A','E','I','O','U'];s=list(input())
for i in  range(len(s)) :
    if s[i] in vowel:   s[i]=s[i].upper()
print("".join(s))