def recursion(s, l, r, cnt):
    if l >= r: return 1, cnt
    elif s[l] != s[r]: return 0, cnt
    else: 
        cnt += 1
        return recursion(s, l+1, r-1, cnt)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

tk = int(input())
for _ in range(tk):
    s = input().rstrip()
    a, b = isPalindrome(s)
    print(a, b)