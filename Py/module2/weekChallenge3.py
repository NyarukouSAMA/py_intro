cusList = [int(i) for i in input().split()]
val = int(input())
isPresent = False
for i in range(len(cusList)):
    if val == cusList[i]:
        isPresent = True
        print(i, end=' ')
if not isPresent:
    print("Отсутствует")