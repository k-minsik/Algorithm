# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# n, m = map(int, input().split())
# arr = [list(input().rstrip()) for _ in range(n)]
# visited = [[0 for _ in range(m)] for _ in range(n)]
# dp = [[0 for _ in range(m)] for _ in range(n)]
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# answer = 0

# def dfs(y, x, cnt):
#     global answer
#     answer = max(answer, cnt)
#     for i in range(4):
#         ny = y + dy[i] * int(arr[y][x])
#         nx = x + dx[i] * int(arr[y][x])

#         if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 'H':
#             if cnt + 1 > dp[ny][nx]:
#                 if visited[ny][nx]:
#                     print(-1)
#                     exit()
#                 else:
#                     visited[ny][nx] = 1
#                     dp[ny][nx] = cnt + 1
#                     dfs(ny, nx, cnt + 1)
#                     visited[ny][nx] = 0


# dfs(0, 0, 0)
# print(answer + 1)

import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
dp = [[0] * c for _ in range(r)]
visited[0][0] = True

def dfs(y, x, cnt):
    global answer

    move = int(graph[y][x])
    for i in range(4):
        ny = y + dy[i] * move
        nx = x + dx[i] * move

        if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 'H':
            if cnt > dp[ny][nx]:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    dp[ny][nx] = cnt
                    dfs(ny, nx, cnt + 1)
                    visited[ny][nx] = False

                else:
                    print(-1)
                    exit()
        else:
            answer = max(answer, cnt)

answer = -1
dfs(0, 0, 1)
print(answer)