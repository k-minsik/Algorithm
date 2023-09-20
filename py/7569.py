import sys
from collections import deque
input = sys.stdin.readline

dy = [1, 0, -1, 0, 0, 0]
dx = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

c, r, h = map(int, input().split())
graph = []
yes = []

for k in range(h):
    box = []

    for i in range(r):
        row = list(map(int, input().split()))
        for j in range(c):
            if row[j] == 1:
                yes.append([k, i, j])

        box.append(row)
    
    graph.append(box)

dq = deque(yes)
answer = -1
while dq:
    z, y, x = dq.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c and 0 <= nz < h:
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                dq.append([nz, ny, nx])

for z in range(h):
    for y in range(r):
        for x in range(c):
            if graph[z][y][x] == 0:
                print(-1)
                exit()
            else:
                answer = max(answer, graph[z][y][x])

print(answer - 1)