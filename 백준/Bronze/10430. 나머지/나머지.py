a,b,c = map(int,input().split())
A = (a+b)%c
B = ((a%c) + (b%c))%c
C = (a*b)%c
D = ((a%c) * (b%c))%c
print(A,B,C,D,sep='\n')