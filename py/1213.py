arr = [0 for _ in range(26)]

s = input().rstrip()

for i in range(len(s)):
    arr[ord(s[i]) - 65] += 1

flag = 0
res = ''
mid = ''

for i in range(26):
    if arr[i] % 2 == 1:
        flag += 1
        if flag == 2:
            break
        mid = chr(i + 65)
    res += chr(i+65) * (arr[i] //2)

if flag == 2: print("I'm Sorry Hansoo")
else: print(res + mid + res[::-1])
