import sys
input = sys.stdin.readline

N = int(input())
dp = [float(input())] + [0] * (N - 1)

for i in range(1, N):
    n = float(input())
    
    dp[i] = max(dp[i-1] * n, n)

print("%.3f" % max(dp))