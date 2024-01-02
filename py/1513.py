import sys
input = sys.stdin.readline

dy = [0, 1]
dx = [1, 0]

n, m, c = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
dp = [[[[-1] * (c + 1) for _ in range(c + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
# dp[y][x][count][where]

for i in range(1, c + 1):
    y, x = map(int, input().split())
    graph[y][x] = i

def dfs(y, x, count, now):
    if not (0 < y < n + 1 and 0 < x < m + 1):
        return 0
    
    if y == n and x == m:
        if count == 0 and not graph[y][x]:
            return 1
        elif count == 1 and graph[y][x] > now:
            return 1
        return 0
    
    if dp[y][x][count][now] != -1:
        return dp[y][x][count][now]
    
    tempAnswer = 0
    for i in range(2):
        ny, nx = y + dy[i], x + dx[i]
        if graph[y][x] == 0:
            tempAnswer += dfs(ny, nx, count, now)
        elif graph[y][x] > now:
            tempAnswer += dfs(ny, nx, count - 1, graph[y][x])

    dp[y][x][count][now] = tempAnswer % 1000007
    return dp[y][x][count][now]

for i in range(c + 1):
    print(dfs(1, 1, i, 0), end = " ")