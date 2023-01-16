n = int(input())
count1 = 0
count2 = 0
for i in range(n):
    truth = int(input())
    if truth == 0:
        count1 += 1
    else:
        count2 += 1
if count1>count2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')