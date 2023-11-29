# x, y = map(int, input().split())
# z = y * 100 // x

# if z >= 99:
#     print(-1)
# else:
#     answer = 0
#     lo = 1
#     hi = x
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         temp = (y + mid) * 100 // (x + mid)

#         if temp > z:
#             answer = mid
#             hi = mid - 1
#         else:
#             lo = mid + 1

#     print(answer)


import sys
input = sys.stdin.readline

x, y = map(int, input().split())
winRate = int(y * 100 / x)

if winRate >= 99:
    print(-1)
    exit()

answer = -1
low, high = 1, int(1e9)
while low <= high:
    mid = (low + high) // 2

    total = x + mid
    win = y + mid
    rate = int(win * 100 / total)

    if rate != winRate:
        high = mid - 1
        answer = mid

    else:
        low = mid + 1

print(answer)