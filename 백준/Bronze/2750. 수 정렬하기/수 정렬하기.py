t = int(input())
box = []
for i in range(t):
    box.append(int(input()))
box = sorted(box)
for i in box:
    print(i)