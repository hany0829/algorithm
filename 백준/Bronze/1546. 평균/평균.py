n=int(input())
score = list(map(int,input().split()))
fake=(max(score))

f_s=[]
for i in score:
    f_s.append(i/fake*100)
avg_li=sum(f_s)/n
print(avg_li)