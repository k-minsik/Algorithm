import sys
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    n, m = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    answer = 0
    for a in A:
        temp = 0
        lo, hi = 0, m - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            if a > B[mid]:
                temp = mid + 1
                lo = mid + 1
            else:
                hi = mid - 1

        answer += temp

    print(answer)