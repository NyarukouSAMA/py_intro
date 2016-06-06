def f(x):
    print()

n = input()
cusDict = {}
for i in range(n):
    x = int(input())
    if x in cusDict:
        print(cusDict.get(x))
    else:
        cusDict[x] = f(x)
        print(cusDict.get(x))