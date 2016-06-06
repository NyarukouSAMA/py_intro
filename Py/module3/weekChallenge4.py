n = int(input())
directionsDict = {'восток':[1],'запад':[-1],'север':[1],'юг':[-1]}
for i in range(n):
    tmpList = [j for j in input().split()]
    directionsDict[tmpList[0]] += [int(tmpList[1]) * directionsDict[tmpList[0]][0]]
resWithX = 0
resWithY = 0
for i in range(1, len(directionsDict['восток'])):
    resWithX += directionsDict['восток'][i]
for i in range(1, len(directionsDict['запад'])):
    resWithX += directionsDict['запад'][i]
for i in range(1, len(directionsDict['север'])):
    resWithY += directionsDict['север'][i]
for i in range(1, len(directionsDict['юг'])):
    resWithY += directionsDict['юг'][i]
print(resWithX, resWithY, sep=' ')