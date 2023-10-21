# n, t = map(int, input().split())
# temp = list(map(int, input().split()))
# presum = [0]

# for i in range(n):
#     presum.append(presum[-1] + temp[i])

# M = -1e9
# for i in range(t, n+1):
#     res = presum[i] - presum[i-t]
#     M = max(M, res)

# print(M)


import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))
accumulatedSum = [0] + [i for i in temperature]

maxSum = -1e9
for i in range(1, n + 1):
    accumulatedSum[i] += accumulatedSum[i - 1]

    if i >= k:
        maxSum = max(maxSum, accumulatedSum[i] - accumulatedSum[i - k])

print(maxSum)