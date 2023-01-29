t=int(input())
for _ in range(t):
    quiz=list(input())
    score=0
    sum=0
    for i in quiz:
        if i=='O':
            score+=1
            sum+=score
        else:
            score=0
    print(sum)