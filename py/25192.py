n = int(input())
d = {}

cnt = 0
for _ in range(n):
    s = input().rstrip()
    if s != "ENTER":
        if s not in d:
            d[s] = 1
            cnt += 1
    else:
        d.clear()
print(cnt)