# import sys
# input = sys.stdin.readline

# n = int(input())
# hp = list(map(int, input().split()))
# joy = list(map(int, input().split()))
# # answer = 0

# # for i in range(1 << n):
# #     hp_ = 100
# #     temp = 0
# #     for j in range(n):
# #         if i & (1 << j):
# #             hp_ -= hp[j]
# #             temp += joy[j]
            
# #             if hp_ <= 0:
# #                 break
# #     if hp_ > 0:
# #         answer = max(answer, temp)

# # print(answer)

# dp = [0 for _ in range(101)]
# for i in range(n):
#     for j in range(100, hp[i], -1):
#         dp[j] = max(dp[j], dp[j - hp[i]] + joy[i])
#     print(dp)
# print(dp[100])


import sys
input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))
gain = list(map(int, input().split()))

life, happy = 100, 0
dp = [0] * 101

for l, g in zip(loss, gain):
    for i in range(100, l, -1):
        dp[i] = max(dp[i], dp[i - l] + g)

print(dp[100])
