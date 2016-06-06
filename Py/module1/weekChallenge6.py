a = int(input())
p = a % 100
if a % 10 == 1 and p != 11:
    print(a, 'программист')
elif a % 10 == 2 and p != 12 or a % 10 == 3 and p != 13 or a % 10 == 4 and p != 14:
    print(a, 'программиста')
else:
    print(a, 'программистов')