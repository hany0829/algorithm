t=int(input())
box=[]
for i in range(t):
    n=int(input())
    if n == 0:
        box.pop()
    else:    
        box.append(n)
print(sum(box))