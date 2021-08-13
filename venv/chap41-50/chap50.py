# python documentation.
import ssl
from urllib import request


target = request.urlopen("http://coupang.com")
content = target.read()

print(content)