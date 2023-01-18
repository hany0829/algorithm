serch_w = input()
word = 'CAMBRIDGE'
new = ''

for i in serch_w:
        if i not in word:
            new += i
print(new)