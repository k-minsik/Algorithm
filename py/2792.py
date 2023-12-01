# import sys
# from math import ceil
# input = sys.stdin.readline

# def check(mid):
#     global n, m
#     num = 0

#     for i in range(m):
#         num += ceil(gem[i] / mid)
    
#     if n >= num:
#         return True
#     else:
#         return False


# n, m = map(int, input().split())
# gem = []
# high = 0
# for _ in range(m):
#     temp = int(input())
#     gem.append(temp)
#     high = max(high, temp)
# low = 1

# answer = int(1e10)
# while low <= high:
#     mid = (low + high) // 2
    
#     if check(mid):
#         answer = min(answer, mid)
#         high = mid - 1
#     else:
#         low = mid + 1

# print(answer)

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
gems = [int(input()) for _ in range(m)]
low, high = 1, max(gems)

answer = 1e9
while low <= high:
    mid = (low + high) // 2

    count = 0
    for gem in gems:
        count += math.ceil(gem / mid)

    if count <= n:
        answer = min(answer, mid)
        high = mid - 1
    else:
        low = mid + 1

print(answer)