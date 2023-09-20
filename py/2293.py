import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)

for c in coin:
    for i in range(k + 1):
        if i == c:
            dp[i] += 1
        elif i > c:
            dp[i] += dp[i - c]

print(dp[k])