t = int(input())
for _ in range(t):
    box = []
    n = int(input())
    box = list(map(int, input().split()))
    result = 0
    for i in box:
        result += i
    print(result)