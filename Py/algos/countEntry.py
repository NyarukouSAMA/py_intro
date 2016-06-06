def countEntry(line):
    cusList = [i for i in line.lower().split()]
    cusSet = set(cusList)
    for i in cusSet:
        print(i, cusList.count(i), sep=' ')

line = input()
countEntry(line)