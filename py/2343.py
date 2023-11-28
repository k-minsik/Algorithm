# import sys
# input = sys.stdin.readline

# def check(mid):
#     global n, m, M

#     if M > mid:
#         return False

#     temp = mid
#     cnt = 0

#     for i in range(n):
#         if temp - data[i] < 0:
#             cnt += 1
#             temp = mid
        
#         temp -= data[i]
    
#     if mid != temp:
#         cnt += 1

#     if cnt <= m:
#         return True
#     else:
#         return False


# n, m = map(int, input().split())
# data = list(map(int, input().split()))
# low = 0
# high = sum(data)
# M = max(data)

# while low <= high:
#     mid = (low + high) // 2

#     if check(mid):
#         high = mid - 1
#         answer = mid
#     else:
#         low = mid + 1

# print(answer)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

l = 1
r = sum(lecture)
M = max(lecture)
answer = -1

while l <= r:
    mid = (l + r) // 2
    if mid < M:
        l = mid + 1
        continue

    disk = mid
    count = 1
    for i in range(n):
        if disk - lecture[i] < 0:
            disk = mid
            count += 1

        disk -= lecture[i]

    if count <= m:
        r = mid - 1
        answer = mid

    else:
        l = mid + 1

print(answer)