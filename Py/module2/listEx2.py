cusList = [int(i) for i in input().split()]
if len(cusList) == 1:
    print(cusList[0])
else:
    for i in range(len(cusList)):
        print(cusList[i - 1] + cusList[-len(cusList) + i + 1], end=' ')