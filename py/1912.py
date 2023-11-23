import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [nums[0]] + [0] * (n - 1)

for i in range(1, n):
    if dp[i - 1] > 0:
        dp[i] = dp[i - 1] + nums[i]
    else:
        dp[i] = nums[i]

print(max(dp))