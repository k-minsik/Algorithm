import sys
input = sys.stdin.readline

n = int(input())
d = {"ChongChong" : 0}
idx = 1

for _ in range(n):
    a, b = input().split()
    if a in d:
        if b not in d:
            d[b] = idx
            idx += 1
    elif b in d:
        if a not in d:
            d[a] = idx
            idx += 1

print(idx)

