import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] + [int(1e9) for _ in range(k)]

for i in range(k + 1):
    for c in coin:
        if i == c:
            dp[i] = 1
        elif i > c:
            dp[i] = min(dp[i], dp[i - c] + 1)

print(dp[k] if dp[k] != 1e9 else -1)