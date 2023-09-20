n = int(input())
a, b, c, d = 1e9, 1e9, -1e9, -1e9
for i in range(n):
    x, y = map(int, input().split())
    a = min(a, x)
    b = min(b, y)
    c = max(c, x)
    d = max(d, y)

print((c - a) * (d - b))
