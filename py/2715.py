import sys
input = sys.stdin.readline

n = int(input())
# arr = [int(input()) for _ in range(n)]

# for i in sorted(arr):
#     print(i)

d = {}
for i in range(1, 10001):
    d[i] = 0

for _ in range(n):
    d[int(input())] += 1

for k, v in d.items():
    for i in range(v):
        print(k)