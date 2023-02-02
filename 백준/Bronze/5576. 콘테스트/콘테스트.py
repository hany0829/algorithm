w=[]
k=[]
for i in range(10):
    w.append(int(input()))
w = sorted(w,reverse=True)
w_total =sum(w[0:3])
    
for i in range(10):
    k.append(int(input()))
k = sorted(k,reverse=True)
k_total =sum(k[0:3])

print(w_total,k_total)
