n = int(input())
dictSet = set()
for i in range(n):
    dictSet.add(input().lower())
l = int(input())
resDict = set()
for i in range(l):
    tmpList = [j for j in input().lower().split()]
    for j in tmpList:
        if j not in dictSet:
            resDict.add(j)
for i in resDict:
    print(i)