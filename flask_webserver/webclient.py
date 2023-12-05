import requests

ip = '192.168.10.10'
port = '8080'
url = 'http://%s:%s' % (ip, port)

resp = requests.get(url)
print(resp.text)

url = 'http://%s:%s/api/data' % (ip, port)
resp = requests.get(url)
print(resp.text)

data = '{"id" : "3", "name" : "ko"}'
requests.post(url, data)
print(resp.text)
