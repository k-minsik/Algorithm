import sys
input = sys.stdin.readline

dy = [0, 1]
dx = [1, 0]

n, m, c = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
dp = [[[[0] * (c + 1) for _ in range(c + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
# dp[y][x][count][where]

for i in range(c):
    y, x = map(int, input().split())
    graph[y][x] = i

def dfs(y, x, cout, now):
    if 0 < y < n + 1 and 0 < x < m + 1:
        return 0
    
    if y == n and x == m:
        

for i in range(c + 1):
    print(dfs(1, 1, i, 0))