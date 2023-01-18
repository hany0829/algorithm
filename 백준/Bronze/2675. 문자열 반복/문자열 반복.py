t = int(input())
for i in range(t):
    num, st = input().split()
    new = ''
    for i in st:
        new += int(num) * i
    print(new)
