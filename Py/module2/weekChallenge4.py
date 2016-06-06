i = 0
cusMtx = []
while True:
    cusStr = input()
    if cusStr == 'end':
        break
    cusMtx += [[int(j) for j in cusStr.split()]]
for i in range(len(cusMtx)):
    for j in range(len(cusMtx[i])):
        print(cusMtx[i - 1][j] + cusMtx[-len(cusMtx) + i + 1][j] + cusMtx[i][j - 1] + cusMtx[i][-len(cusMtx[i]) + j + 1], end=' ')
    print()