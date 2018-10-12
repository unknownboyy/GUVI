import bcookie as browser_cookie3
import requests
from Block import Block
from datetime import datetime

b1=Block.create_genesis_block()

cj=browser_cookie3.chrome()
"""
r = requests.get("http://myblockchainserver1.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=cj)
print(r.content,r.status_code,r.cookies)
"""
import urllib.request
public_html = urllib.request.urlopen('http://myblockchainserver1.epizy.com/phpclass1.php').read()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))