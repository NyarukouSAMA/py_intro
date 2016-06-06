def countEntry(line):
    cusList = [i for i in line.lower().split()]
    cusSet = set(cusList)
    for i in cusSet:
        if i not in cusDict:
            cusDict[i] = cusList.count(i)
        else:
            cusDict[i] += cusList.count(i)

cusDict = {}
with open('../files/dataset_3363_3.txt') as inFile:
    for line in inFile:
        countEntry(line.strip())
maxVal = max(cusDict.values())
maxVal = min({key : maxVal for key in cusDict if cusDict[key] == maxVal})
print(maxVal, cusDict[maxVal])