import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][1] = 1
q = deque([[0, 0, 1]])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
flag = 1
while q:
    y, x, c = q.popleft()

    if y == n - 1 and x == m - 1:
        flag = 0
        print(visited[y][x][c])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:

            if graph[ny][nx] == '0' and visited[ny][nx][c] == 0:
                q.append([ny, nx, c])
                visited[ny][nx][c] = visited[y][x][c] + 1

            if graph[ny][nx] == '1' and c == 1:
                q.append([ny, nx, c - 1])
                visited[ny][nx][c - 1] = visited[y][x][c] + 1
            
if flag:
    print(-1)