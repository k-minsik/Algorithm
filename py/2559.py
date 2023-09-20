n, t = map(int, input().split())
temp = list(map(int, input().split()))
presum = [0]

for i in range(n):
    presum.append(presum[-1] + temp[i])

M = -1e9
for i in range(t, n+1):
    res = presum[i] - presum[i-t]
    M = max(M, res)

print(M)

