n, c = map(int, input().split())
arr = list(map(int, input().split()))

cnt = {}

for i in range(len(arr)):
    if arr[i] in cnt:
        cnt[arr[i]][0] += 1
    else:
        cnt[arr[i]] = [1, i]

cnt = sorted(cnt.items(), key = lambda x: (-x[1][0], x[1][1]))

for k, v in cnt:
    for _ in range(v[0]):
        print(k, end = ' ')

