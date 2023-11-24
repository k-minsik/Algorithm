# import sys
# input = sys.stdin.readline

# s, c = map(int, input().split())
# arr = [int(input()) for _ in range(s)]
# lo, hi = 1, max(arr)

# answer = 0
# while lo <= hi:
#     mid = (lo + hi) // 2

#     cnt = sum(i // mid for i in arr)
#     if cnt >= c:
#         lo = mid + 1
#         answer = mid
#     else:
#         hi = mid - 1

# print(sum(arr) - (answer * c))

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
pas = [int(input()) for _ in range(n)]
l, r = 1, max(pas)

while l <= r:
    mid = (l + r) // 2

    make = 0
    for pa in pas:
        make += pa // mid

        if make > k:
            break
    
    if make >= k:
        l = mid + 1
        answer = mid
    elif make < k:
        r = mid - 1

print(sum(pas) - k * answer)