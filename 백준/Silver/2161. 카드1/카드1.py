dc=[]
n=int(input())
queue=list(range(1,n+1))
while len(queue) !=1:
    dc.append(queue.pop(0))
    queue.append(queue.pop(0))
print(*dc,queue[0])
