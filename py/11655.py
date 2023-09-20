res = ''
s = list(input().rstrip())

for i in range(len(s)):
    if s[i].islower():
        temp = ord(s[i]) + 13
        if temp > 122:
            temp -= 26
        s[i] = chr(temp)
    elif s[i].isupper():
        temp = ord(s[i]) + 13
        if temp > 90:
            temp -= 26
        s[i] = chr(temp)
    
    print(s[i], end='')

