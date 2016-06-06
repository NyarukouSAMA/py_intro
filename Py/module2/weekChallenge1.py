cusSum = int(input())
sqSum = cusSum ** 2
while cusSum != 0:
    val = int(input())
    cusSum += val
    sqSum += val ** 2
print(sqSum)