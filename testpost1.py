import http.client
import ssl

connection = http.client.HTTPSConnection("www.myblockchainserver1.ezyro.com",context=ssl._create_unverified_context())
connection.request("GET", "/phpclass1.php")
response = connection.getresponse()
print("Status: {} and reason: {} ".format(response.status, response.reason))
print(response.read())

connection.close()

"""import requests
r = requests.get('https://api.github.com/events')
print(r.status_code,r.content,r.cookies)
"""
"""
import execjs
from http.cookiejar import CookieJar
from Block import Block
from datetime import datetime
import execjs.runtime_names
jscript = execjs.get(execjs.runtime_names.JScript)

jscript.eval('function toNumbers(d){var e=[];d.replace(/(..)/g,function(d){e.push(parseInt(d,16))});return e}function toHex(){for(var d=[],d=1==arguments.length&&arguments[0].constructor==Array?arguments[0]:arguments,e="",f=0;f<d.length;f++)e+=(16>d[f]?"0":"")+d[f].toString(16);return e.toLowerCase()}var a=toNumbers("f655ba9d09a112d4968c63579db590b4"),b=toNumbers("98344c2eee86c3994890592585b49f80"),c=toNumbers("92e3ac534536c95b356b6243f680cbe7");toHex(slowAES.decrypt(c,2,a,b));')

b1=Block.create_genesis_block()
s=requests.Session()
r = requests.get("http://myblockchainserver1.ezyro.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash})
coo=r.cookies
print(r.status_code,r.content,*coo)
"""
"""
r = requests.post("http://myblockchainserver1.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)
print(r.status_code, r.reason,r.content)
"""
"""
r = requests.post("http://myblockchainserver4.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)
print(r.status_code, r.reason,r.content)

r = requests.post("http://myblockchainserver3.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)

print(r.status_code, r.reason,r.content)

b1=Block(b1.hash,"hello",datetime.now())

r = requests.post("http://myblockchainserver1.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)
print(r.status_code, r.reason,r.content)

r = requests.post("http://myblockchainserver4.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)
print(r.status_code, r.reason,r.content)

r = requests.post("http://myblockchainserver3.epizy.com/phpclass1.php", data={'a': b1.previous_block_hash, 'b': b1.data, 'c': b1.timestamp,"d":b1.hash},cookies=coo)

print(r.status_code, r.reason,r.content)
"""