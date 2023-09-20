import sys
input = sys.stdin.readline

cnt = [0] * 26
s = list(input().strip())

for i in s:
    cnt[ord(i) - 97] += 1

for i in cnt:
    print(i, end=' ')
    
