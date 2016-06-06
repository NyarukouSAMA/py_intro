sourceAlphabet = [i for i in input()]
destAlphabet = [i for i in input()]
key = {sourceAlphabet[i] : destAlphabet[i] for i in range(len(sourceAlphabet))}
strForEncrypt = input()
encryptedStr = ''
strForDecrypt = input()
decryptedStr = ''
for i in strForEncrypt:
    encryptedStr += key[i]
for i in strForDecrypt:
    for j, value in key.items():
        if i == value:
            decryptedStr += j
print(encryptedStr)
print(decryptedStr)