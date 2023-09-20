dp = [0 for _ in range(12)]
dp[1], dp[2], dp[3], dp[4] = 1, 2, 4, 7

for i in range(5, 12):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in range(int(input())):
    print(dp[int(input())])
