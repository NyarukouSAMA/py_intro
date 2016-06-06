n = int(input())
cusList = [[0 for j in range(n)] for i in range(n)]
curVal = 1
curCoil = 0
while curVal <= n ** 2:
    for i in range(curCoil, n - curCoil - 1):
        cusList[curCoil][i] = curVal
        cusList[i][n - curCoil - 1] = curVal + (n - curCoil * 2 - 1)
        cusList[n - curCoil - 1][-i-1] = curVal + (n - curCoil * 2 - 1)*2
        cusList[-i-1][curCoil] = curVal + (n - curCoil * 2 - 1)*3
        curVal += 1
    curVal += (n - curCoil * 2 - 1)*3
    if curVal != 1:
        curCoil += 1
    if curVal == n ** 2:
        cusList[curCoil][curCoil] = curVal
        break
for i in range(n):
    for j in range(n):
        print(cusList[i][j], end=' ')
    print()