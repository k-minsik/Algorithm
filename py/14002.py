import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1] * n
subSequence = [[nums[i]] for i in range(n)]
print(subSequence)
for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            subSequence[i] = subSequence[j] + [nums[i]]

answer = max(dp)
print(answer)
print(*subSequence[dp.index(answer)])