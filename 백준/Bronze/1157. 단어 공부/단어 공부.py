a = input().upper()
a_li = list(set(a))

n=[]
for i in a_li:
    cnt = a.count(i)
    n.append(cnt)

if n.count(max(n)) > 1:
    print('?')
else:
    max_index = n.index(max(n))
    print(a_li[max_index])