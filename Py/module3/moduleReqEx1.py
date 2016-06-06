import requests

req = requests.get('http://www.zalgotext.net/')
fOut = open('../files/htmlRequestVk.txt', 'w')
fOut.write(req.text)