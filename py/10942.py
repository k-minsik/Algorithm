import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for c in range(1, n + 1):
    for r in range(1, c + 1):
        
        if r == c:
            dp[r][c] = 1
        
        elif arr[r] == arr[c]:
            if r + 1 == c:
                dp[r][c] = 1
            
            elif dp[r + 1][c - 1] == 1:
                dp[r][c] = 1

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[a][b])