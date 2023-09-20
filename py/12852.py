n = int(input())
dp = [(i - 1) for i in range(n + 1)]

for i in range(2, n + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])

    dp[i] = min(dp[i - 1] + 1, dp[i])

print(dp[n])

while True:
    if n == 1:
        print(1)
        break
    print(n, end = " ")

    if n % 3 == 0 and dp[n] == dp[n // 3] + 1:
        n //= 3
    elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
        n //= 2
    else:
        n -= 1
    