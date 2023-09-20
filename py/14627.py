import sys
input = sys.stdin.readline

s, c = map(int, input().split())
arr = [int(input()) for _ in range(s)]
lo, hi = 1, max(arr)

answer = 0
while lo <= hi:
    mid = (lo + hi) // 2

    cnt = sum(i // mid for i in arr)
    if cnt >= c:
        lo = mid + 1
        answer = mid
    else:
        hi = mid - 1

print(sum(arr) - (answer * c))