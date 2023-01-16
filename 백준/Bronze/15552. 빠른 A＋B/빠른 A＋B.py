import sys
sum=0
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    sum+=1
    print(a+b)
