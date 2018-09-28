import hashlib
def hashCode(li):
    x=hashlib.sha1()
    x.update(repr(li).encode('utf-8'))
    return x.hexdigest()
li="hello"
print(hashCode(li))