t=int(input())

word=[]
for _ in range(t):
    s=input()
    word.append(s)

set_word = set(word)
word=list(set_word)
word.sort()
word.sort(key = lambda x:len(x))

print(*word,sep='\n')