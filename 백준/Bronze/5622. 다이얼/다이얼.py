phone = {
    'ABC' : '3', 'DEF':'4','GHI':'5','JKL':'6',
    'MNO':'7','PQRS':'8','TUV':'9','WXYZ':'10',
}
total = 0
string = input()
for k in string:
    for j in phone:
        if k in j:
            total += int(phone[j])
print(total)
