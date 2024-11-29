from urllib import request, parse

data = bytes(parse.urlencode({'name': 'germey'}), encoding= 'utf-8')
res = request.urlopen('https://www.httpbin.org/post', data= data)
print(res.read().decode('utf-8'))