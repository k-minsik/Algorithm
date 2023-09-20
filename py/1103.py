import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def dfs(y, x, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        ny = y + dy[i] * int(arr[y][x])
        nx = x + dx[i] * int(arr[y][x])

        if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 'H':
            if cnt + 1 > dp[ny][nx]:
                if visited[ny][nx]:
                    print(-1)
                    exit()
                else:
                    visited[ny][nx] = 1
                    dp[ny][nx] = cnt + 1
                    dfs(ny, nx, cnt + 1)
                    visited[ny][nx] = 0


dfs(0, 0, 0)
print(answer + 1)