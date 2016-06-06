import requests

fIn = open('../files/dataset_3378_3.txt')
s = fIn.read().strip()
fIn.close()
urlList = [i for i in s.split('/')]
firtsWord = 'We'
while True:
    r = requests.get(s)
    s = r.text
    print(s)
    if firtsWord in s:
        fOut = open('../files/modReqEx3Out.txt', 'w')
        fOut.write(s)
        break
    else:
        tmpListUrlCh = [i for i in s.strip().split('/')]
        for i in range(len(tmpListUrlCh)):
            urlList[-1 - i] = tmpListUrlCh[-1 - i]
        s = ''
        for i in range(len(urlList) - 1):
            s += urlList[i] + '/'
        s += urlList[len(urlList) - 1]