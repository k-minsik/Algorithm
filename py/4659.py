# mo = ['a', 'e', 'i', 'o', 'u']

# while True:
#     s = input().rstrip()
#     if s == "end":
#         break

#     flag = 0
#     flag2 = 1
#     cnt_mo = 0
#     cnt_ja = 0
#     prev = -1
#     for i in range(len(s)):
#         if i >= 1 and s[prev] == s[i] and s[i] != 'e' and s[i] != 'o':
#             flag2 = 0
#             break

#         if s[i] in mo:
#             flag = 1
#             cnt_mo += 1
#             cnt_ja = 0
#         else:
#             cnt_ja += 1
#             cnt_mo = 0

#         if cnt_ja >= 3 or cnt_mo >= 3:
#             flag2 = 0
#             break
#         prev = i
    
#     if flag and flag2:
#         print("<" + s + ">" + " is acceptable")
#         continue
#     else:
#         print("<" + s + ">" + " is not acceptable")
#         continue


import sys
input = sys.stdin.readline

aeiou = ['a', 'e', 'i', 'o', 'u']
while True:
    password = input().rstrip()
    
    if password == "end":
        break

    countMo = 1 if password[0] in aeiou else 0
    countJa = 0 if countMo else 1
    flag = True if password[0] in aeiou else False

    for i in range(1, len(password)):
        if password[i] in aeiou:
            countMo += 1
            countJa = 0
            flag = True
        else:
            countJa += 1
            countMo = 0

        if (password[i] == password[i - 1]) and password[i] not in ['e', 'o']:
            flag = False
            break

        if countJa >= 3 or countMo >= 3:
            flag = False
            break

    valid = "acceptable." if flag else "not acceptable"
    print("<" + password + "> is " + valid)