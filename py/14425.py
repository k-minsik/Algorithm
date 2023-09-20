import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for _ in range(n):
    d[input().rstrip()] = 1

ret = 0
for _ in range(m):
    if input().rstrip() in d:
        ret += 1

print(ret)