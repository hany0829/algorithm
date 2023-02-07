import sys
input = sys.stdin.readline

n = int(input())
stick = []
cnt = 1

for _ in range(n):
    num = int(input())
    stick.append(num)

top = stick[-1]    
for i in range(len(stick)-1,-1,-1):
    if stick[i] > top:
        cnt += 1
        top = stick[i]
print(cnt)