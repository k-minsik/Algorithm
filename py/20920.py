import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}

for _ in range(n):
    s = input().rstrip()

    if len(s) >= m:
        if s in d:
            d[s][0] += 1
        else:
            d[s] = [1, len(s), s]

d = sorted(d.items(), key = lambda x : (-x[1][0], -x[1][1], x[1][2]))
for k, v in d:
    print(k)