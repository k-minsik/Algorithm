import sys
input = sys.stdin.readline

s = input().rstrip()

arr = set()
for i in range(len(s)):
    for j in range(1, len(s)+1):
        arr.add(s[i:j])

print(len(arr) - 1)