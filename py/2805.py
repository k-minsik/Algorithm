import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, max(arr) - 1

while l <= r:
    temp = 0
    mid = (l + r) // 2

    for i in arr:
        if i > mid:
            temp += i - mid

    if temp < m:
        r = mid - 1
    else:
        l = mid + 1

print(r)
