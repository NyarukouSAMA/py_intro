cusList = []
with open('../files/dataset_3363_4.txt') as inFile:
    for line in inFile:
        cusList += [[i for i in line.strip().split(';')]]
overAllPerf = []
for i in range(len(cusList)):
    stuPerf = 0
    countSubj = 0
    for j in range(1, len(cusList[i])):
        val = int(cusList[i][j])
        countSubj += 1
        if len(overAllPerf) < j:
            overAllPerf += [val]
        else:
            overAllPerf[j-1] = (overAllPerf[j-1] * i + val) / (i + 1)
        stuPerf += val
    print(stuPerf/countSubj)
for i in overAllPerf:
    print(i, end=' ')