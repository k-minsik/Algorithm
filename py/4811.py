# import sys
# input = sys.stdin.readline

# while True:
#     n = int(input())
#     if n == 0:
#         break
    
#     dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#     for i in range(1, n + 1):
#         dp[i][0] = 1

#     for w in range(1, n + 1):
#         for h in range(1, w + 1):
#             dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

#     print(dp[n][n])


import sys
input = sys.stdin.readline

dp = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    dp[i][0] = 1

for w in range(1, 31):
    for h in range(1, w + 1):
        dp[w][h] = dp[w - 1][h] + dp[w][h - 1]

while True:
    n = int(input())
    if n == 0:
        break
    
    print(dp[n][n])