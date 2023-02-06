people = []
result = 0

for i in range(4):
    a, b = map(int,input().split())
    result=result-a+b
    people.append(result)

print(max(people))