import requests

fIn = open('../files/dataset_3378_2.txt')
s = fIn.read().strip()
fIn.close()
r = requests.get(s)
print(len(r.text.splitlines()))