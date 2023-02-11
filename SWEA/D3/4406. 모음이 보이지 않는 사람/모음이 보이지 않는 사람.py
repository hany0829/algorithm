T = int(input())
for tc in range(1, T+1):
    word = input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    answer =''

    for i in word:
        if i not in vowel:
            answer += i
    
    print(f'#{tc}',answer)