num_li=[]
for i in range(10):
    n=int(input())
    num_li.append(n%42)
num_li=set(num_li)
print(len(num_li))