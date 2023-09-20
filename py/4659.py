mo = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input().rstrip()
    if s == "end":
        break

    flag = 0
    flag2 = 1
    cnt_mo = 0
    cnt_ja = 0
    prev = -1
    for i in range(len(s)):
        if i >= 1 and s[prev] == s[i] and s[i] != 'e' and s[i] != 'o':
            flag2 = 0
            break

        if s[i] in mo:
            flag = 1
            cnt_mo += 1
            cnt_ja = 0
        else:
            cnt_ja += 1
            cnt_mo = 0

        if cnt_ja >= 3 or cnt_mo >= 3:
            flag2 = 0
            break
        prev = i
    
    if flag and flag2:
        print("<" + s + ">" + " is acceptable")
        continue
    else:
        print("<" + s + ">" + " is not acceptable")
        continue





