cup=[1,2,3]
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    c1=cup.index(x)
    c2=cup.index(y)
    cup[c1],cup[c2] = cup[c2],cup[c1]

print(cup[0])