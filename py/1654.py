import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
m = -1

for _ in range(n):
    temp = int(input())
    arr.append(temp)
    if temp > m:
        m = temp

l, r = 1, m

while l <= r:
    m = (l + r) // 2
    cnt = 0
    for i in arr:
        cnt += i // m

    if cnt >= k:
        l = m + 1
    else:
        r = m - 1

print(r)

