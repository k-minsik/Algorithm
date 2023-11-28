# import sys
# input = sys.stdin.readline

# def check(mid):
#     global n, m

#     now = mid
#     cnt = 1
#     for i in range(n):
#         if now - arr[i] < 0:
#             now = mid
#             cnt += 1
        
#         now -= arr[i]
        
#     if cnt <= m:
#         return True
#     else:
#         return False


# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))

# low = max(arr)
# high = int(1e10)

# answer = low
# while low <= high:
#     mid = (low + high) // 2

#     if check(mid):
#         answer = mid
#         high = mid - 1
#     else:
#         low = mid + 1

# print(answer)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]

M = max(money)
low = M
high = int(1e9)
answer = M 

while low <= high:
    mid = (low + high) // 2
    if mid < M:
        low = mid + 1

    count = 1
    have = mid
    for i in range(n):
        if have - money[i] < 0:
            have = mid
            count += 1

        have -= money[i]

    if count <= m:
        high = mid - 1
        answer = mid

    elif count > m:
        low = mid + 1

print(answer)