import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
visited = [[0 for _ in range(c)] for _ in range(r)]
graph = []
ret = [[-1 for _ in range(c)] for _ in range(r)]
dq = deque()

for i in range(r):
    temp = list(map(int, input().split()))
    
    for j in range(c):
        if temp[j] == 2:
            dq.append([i, j])
            ret[i][j] = 0
        elif temp[j] == 0:
            ret[i][j] = 0

    graph.append(temp)

while dq:
    y, x = dq.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
            if graph[ny][nx] == 1:
                ret[ny][nx] = ret[y][x] + 1
                visited[ny][nx] = 1
                dq.append([ny, nx])

for i in range(r):
    for j in range(c):
        print(ret[i][j], end = ' ')
    print()