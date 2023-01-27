duck=[]
start=input()
while start=='고무오리 디버깅 시작':
    word=input()
    if word=="문제":
        duck.append(1)
    elif word=="고무오리":
        if len(duck)==0:
            duck.append(1)
            duck.append(1)
        else:
            duck.pop()
            
    elif word=="고무오리 디버깅 끝":
        break

if 1 not in duck:
    print("고무오리야 사랑해")
else:
    print("힝구")