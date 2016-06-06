def unpack(line):
    i = 0
    numStr = '0123456789'
    newLine = ''
    while i < len(line):
        s = line[i]
        i += 1
        num = ''
        while i < len(line) and line[i] in numStr:
            num += line[i]
            i += 1
        for j in range(int(num)):
            newLine += s
    return newLine

outFile = open('someFileOut.txt', 'w')
with open('dataset_3363_2.txt') as inFile:
    for line in inFile:
        line = line.strip()
        lineOut = unpack(line) + '\n'
        outFile.write(lineOut)
outFile.close()