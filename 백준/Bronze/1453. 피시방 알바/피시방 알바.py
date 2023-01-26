n = int(input())
customer = list(map(int,input().split()))
seat = []
reject = 0
for i in range(n):
    if customer[i] not in seat:
        seat.append(customer[i])
    else:
        reject +=1
print(reject)