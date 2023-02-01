n=int(input())
while 1:
    if len(str(n)) == str(n).count('4')+str(n).count('7'):
        print(n)
        break
    n-=1
