import sys
input = sys.stdin.readline

n = int(input())
d = {}

for _ in range(n):
    a, b = input().split()
    if b == "enter":
        d[a] = 1
    else:
        del d[a]

for i in sorted(d.keys(), reverse=True):
    print(i)
