#print(sum([int(i) for i in input().split()])) - решение в 1 строку, ЛОЛ

cusList = [int(i) for i in input().split()]
cusSum = 0
for i in cusList:
    cusSum += i
print(cusSum)