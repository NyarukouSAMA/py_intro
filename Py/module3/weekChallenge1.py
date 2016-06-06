n = int(input())
resTable = {}
for i in range(n):
    match = [j for j in input().split(';')]
    if int(match[1]) == int(match[3]):
        for j in range(0, len(match), 2):
            if match[j] in resTable:
                tmpTbl = resTable.get(match[j])
                tmpTbl[0] += 1
                tmpTbl[2] += 1
                tmpTbl[4] += 1
                resTable[match[j]] = tmpTbl
            else:
                tmpTbl = [1, 0, 1, 0, 1]
                resTable[match[j]] = tmpTbl
        continue
    elif int(match[1]) > int(match[3]):
        winner = match[0]
        looser = match[2]
    else:
        winner = match[2]
        looser = match[0]
    if winner in resTable:
        tmpTbl = resTable.get(winner)
        tmpTbl[0] += 1
        tmpTbl[1] += 1
        tmpTbl[4] += 3
        resTable[winner] = tmpTbl
    else:
        tmpTbl = [1, 1, 0, 0, 3]
        resTable[winner] = tmpTbl
    if looser in resTable:
        tmpTbl = resTable.get(looser)
        tmpTbl[0] += 1
        tmpTbl[3] += 1
        resTable[looser] = tmpTbl
    else:
        tmpTbl = [1, 0, 0, 1, 0]
        resTable[looser] = tmpTbl
for i in resTable:
    print(i, end=':')
    for j in resTable[i]:
        print(j, end=' ')
    print()