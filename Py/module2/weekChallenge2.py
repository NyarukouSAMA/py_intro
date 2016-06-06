n = int(input())
i = 0
val = 0
while i < n:
    val += 1
    rnVal = 0
    if i + val > n:
        rnVal = (i + val) - n
    for j in range(val - rnVal):
        print(val, end=' ')
    i += val