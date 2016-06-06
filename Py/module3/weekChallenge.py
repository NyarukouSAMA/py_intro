resDict = {i+1 : [] for i in range(11)}
with open('../files/dataset_3380_5.txt') as inFile:
    for line in inFile:
        tmpList = [i for i in line.split('\t')]
        resDict[int(tmpList[0])] += [int(tmpList[2])]
for i in resDict:
    everageHight = 0
    if not resDict[i]:
        print(i, '-', sep=' ')
    else:
        for j in resDict[i]:
            everageHight += j
        everageHight = float(everageHight) / len(resDict[i])
        print(i, everageHight, sep=' ')