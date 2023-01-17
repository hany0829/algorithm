t = int(input())
n = list(map(int, input().split()))
big = n[0]
small = n[0]
for i in n[1:]:
    if i > big:
        big = i
    elif i < small:
        small = i
print(small, big)
        