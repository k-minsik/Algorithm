n = int(input())

cnt = {}
res = ''
for _ in range(n):
    mem = input().strip()
    if mem[0] in cnt:
        cnt[mem[0]] += 1
    else:
        cnt[mem[0]] = 1

cnt = dict(sorted(cnt.items(), reverse=False))
for k, v in cnt.items():
    if v > 4:
        res += k

print(res) if res else print('PREDAJA')
