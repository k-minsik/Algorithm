# import sys
# input = sys.stdin.readline

# while True:
#     n, m = map(float, input().split())
#     if n == 0 and m == 0.00:
#         break

#     n, m = int(n), int(m * 100 + 0.5)
#     dp = [0 for _ in range(m + 1)]
#     for i in range(n):
#         c, p = map(float, input().split())
#         c, p = int(c), int(p * 100 + 0.5)
#         for m in range(p, m + 1):
#             dp[m] = max(dp[m], dp[m - p] + c)

#     print(dp[m])


import sys
input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    if n == 0 and m == 0.00:
        break

    m = int(m * 100 + 0.1)
    dp = [0] * (m + 1)

    for _ in range(int(n)):
        c, p  = map(float, input().split())
        c, p = int(c), int(p * 100 + 0.1)

        for i in range(p, m + 1):
            dp[i] = max(dp[i], dp[i - p] + c)

    print(dp[m])