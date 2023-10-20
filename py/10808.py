# import sys
# input = sys.stdin.readline

# cnt = [0] * 26
# s = list(input().strip())

# for i in s:
#     cnt[ord(i) - 97] += 1

# for i in cnt:
#     print(i, end=' ')
    
import sys
input = sys.stdin.readline

s = input().rstrip()
count = [0 for _ in range(26)]

for i in s:
    count[ord(i) - 97] += 1

for i in count:
    print(i, end = ' ')