import requests
from Block import Block
from datetime import datetime
b1=Block.create_genesis_block()
coo={"__test":"f1b0e7aa289ab05dba72ca7b0f8dac9c"}
file=open('myblocks.txt')
for i in file:
    address=i
add=address.split(",")
print(*add)
for i in add:
    try:
        r = requests.post(i, data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash})
        print(r.status_code, r.reason,r.content)
    except:
        print('Error in ',i)