a = int(input())
b = int(input())
c = a * b
if b > a:
    a ^= b
    b ^= a
    a ^= b
while b > 0:
    a %= b
    a ^= b
    b ^= a
    a ^= b
print(c // a)
