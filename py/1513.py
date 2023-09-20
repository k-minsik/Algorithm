import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
arr = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp = [[[[-1 for _ in range(c + 1)] for _ in range(c + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, c + 1):
    a, b = map(int, input().split())
    arr[a][b] = i

def go(y, x, cnt, now):
    if not (1 <= y <= n and 1 <= x <= m):
        return 0
    else:
        if y == n and x == m:
            if cnt == 0 and not arr[y][x]:
                return 1
            if cnt == 1 and arr[y][x] > now:
                return 1
        
        if dp[y][x][cnt][now] != -1:
            return dp[y][x][cnt][now]

        dp[y][x][cnt][now] = 0
        if arr[y][x] == 0:
            dp[y][x][cnt][now] += (go(y + 1, x, cnt, now) + go (y, x + 1, cnt, now)) % 1000007
        elif arr[y][x] > now:
            dp[y][x][cnt][now] += (go(y + 1, x, cnt - 1, arr[y][x]) + go (y, x + 1, cnt - 1, arr[y][x])) % 1000007

        return dp[y][x][cnt][now]

for i in range(c + 1):
    print(go(1, 1, i, 0), end = " ")