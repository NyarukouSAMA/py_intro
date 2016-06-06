s = input()
i = 0
while i < len(s):
    tmpS = s[i]
    count = 0
    while i + count < len(s) and s[i + count] == tmpS:
        count += 1
    print(tmpS + str(count), end='')
    i += count