# n = int(input())
# dp = [(i - 1) for i in range(n + 1)]

# for i in range(2, n + 1):
#     if i % 3 == 0:
#         dp[i] = min(dp[i // 3] + 1, dp[i])
#     if i % 2 == 0:
#         dp[i] = min(dp[i // 2] + 1, dp[i])

#     dp[i] = min(dp[i - 1] + 1, dp[i])

# print(dp[n])

# while True:
#     if n == 1:
#         print(1)
#         break
#     print(n, end = " ")

#     if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
#         n //= 3
#     elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
#         n //= 2
#     else:
#         n -= 1
    

import sys
input = sys

n = int(input())
dp = [i - 1 for i in range(n + 1)]

for i in range(2, n + 1):
    if not i % 3:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if not i % 2:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[n])

while True:
    if n == 1:
        print(1)
        break

    print(n, end = " ")

    if not n % 3 and dp[n // 3] + 1 == dp[n]:
        n //= 3
    elif not n % 2 and dp[n // 2] + 1 == dp[n]:
        n //= 2
    else:
        n -= 1