t=int(input())
for _ in range(t):
    stack = []
    s = input()
    for i in s:
        if i == '(':
            stack.append(i)
        elif i ==')':
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) == 0:
            print('YES')
        elif len(stack) > 0:
            print('NO')