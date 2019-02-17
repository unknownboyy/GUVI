try:
    s = input()
    w = set()
    for i in s:
        if ord(i)<97 or ord(i)>122:
            raise EnvironmentError
        else:
            w.add(i)
    print('yes') if len(w)==26 else print('no')
except:
    print('Invalid Input')