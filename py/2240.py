# import sys
# input = sys.stdin.readline

# t, w = map(int, input().split())
# arr = [0] + [int(input()) for _ in range(t)]
# dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

# for i in range(t + 1):
#     if arr[i] == 1:
#         dp[i][0] = dp[i - 1][0] + 1
#     else:
#         dp[i][0] = dp[i - 1][0]

    
#     for j in range(1, w + 1):
#         if arr[i] == 1 and j % 2 == 0:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
#         elif arr[i] == 2 and j % 2 == 1:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

# print(max(dp[-1]))
        

import sys
input = sys.stdin.readline

t, w = map(int, input().split())
jadu = [int(input()) for _ in range(t)]
dp = [[0] * (w + 1) for _ in range(t)]

if jadu[0] == 1:
    dp[0][0] = 1
else:
    dp[0][0] = 0

# for i in range(1, t):
#     if jadu[i] == 1:
#         dp[i][0] = dp[i - 1][0] + 1
#     elif jadu[i] == 2:
#         dp[i][0] = dp[i - 1][0]

#     for j in range(1, w + 1):
#         if jadu[i] == 1 and j % 2 == 1:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
#         elif jadu[i] == 2 and j % 2 == 0:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

#             # 나머지 부분은 동일

# for i in range(1, t):
#     if jadu[i] == 1:
#         dp[i][0] = dp[i - 1][0] + 1
#     else:
#         dp[i][0] = dp[i - 1][0]

#     for j in range(1, w + 1):  # 수정된 부분
#         if j >= 1:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
#         if jadu[i] == 1 and j % 2 == 0:  # 수정된 부분
#             dp[i][j] += 1
#         elif jadu[i] == 2 and j % 2 == 1:  # 수정된 부분
#             dp[i][j] += 1

# # 나머지 부분은 동일

for i in range(1, t):
    if jadu[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    elif jadu[i] == 2:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, w + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
        if jadu[i] == 1 and not j % 2:
            dp[i][j] += 1
        elif jadu[i] == 2 and j % 2:
            dp[i][j] += 1



print(max(dp[-1]))