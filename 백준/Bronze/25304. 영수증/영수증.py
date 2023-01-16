price = 0
total = int(input())
num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    price += a*b
if price == total:
    print('Yes')
else:
    print('No')