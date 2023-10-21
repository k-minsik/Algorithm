# res = ''
# s = list(input().rstrip())

# for i in range(len(s)):
#     if s[i].islower():
#         temp = ord(s[i]) + 13
#         if temp > 122:
#             temp -= 26
#         s[i] = chr(temp)
#     elif s[i].isupper():
#         temp = ord(s[i]) + 13
#         if temp > 90:
#             temp -= 26
#         s[i] = chr(temp)
    
#     print(s[i], end='')


import sys
input = sys.stdin.readline

s = list(input().rstrip())

for i in range(len(s)):
    # A-Z = 65-90 , a-z = 97-122
    if 'A' <= s[i] <= 'Z':
        s[i] = chr((ord(s[i]) - ord('A') + 13) % 26 + ord('A'))
    elif 'a' <= s[i] <= 'z':
        s[i] = chr((ord(s[i]) - ord('a') + 13) % 26 + ord('a'))

print(''.join(s))
