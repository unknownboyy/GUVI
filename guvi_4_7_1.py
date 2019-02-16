try:
    s1 = input()
    s2 = input()
    w = ""
    i=0
    while len(s1)>i and len(s2)>i:
        w+=chr(97+(ord(s1[i])+ord(s2[i])-97-97+1)%26);i+=1
    while i<len(s1):
        w+=s1[i];i+=1
    while i<len(s2):
        w+=s2[i];i+=1
    print(w)
except:
    print('Invalid Input')