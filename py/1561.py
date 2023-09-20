import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

lo, hi = 1, int(6e12)
while lo <= hi:
    mid = (lo + hi) // 2

    cnt = sum(mid // i for i in arr)
    if cnt >= n:
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1
