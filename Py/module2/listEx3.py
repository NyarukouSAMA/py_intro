cusList = [int(i) for i in input().split()]
cusList.sort()
i = 0
while i < len(cusList):
    cnt = cusList.count(cusList[i])
    if cnt > 1:
        print(cusList[i], end=' ')
    i += cnt