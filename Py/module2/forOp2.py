a = int(input())
b = int(input())
if a % 3 != 0:
    a += 3 - a % 3
s = 1
for i in range(a + 3, b + 1, 3):
    a += i
    s += 1
print(a / s)