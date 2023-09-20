import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for _ in range(n):
    d[input().rstrip()] = 1

cnt = 0
arr = []
for _ in range(m):
    temp = input().rstrip()
    if temp in d:
        cnt += 1
        arr.append(temp)

print(cnt)
for i in sorted(arr):
    print(i)