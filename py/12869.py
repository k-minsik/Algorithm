import sys
from collections import deque
input = sys.stdin.readline

arr = [[9, 3, 1], [9, 1, 3], 
[3, 9, 1], [3, 1, 9], 
[1, 9, 3], [1, 3, 9]]

n = int(input())
scv = list(map(int, input().split()))
for _ in range(3-n):
    scv.append(0)
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dq = deque()

dq.append(scv)
visited[scv[0]][scv[1]][scv[2]] = 1

while dq:
    x, y, z = dq.popleft()
    if(visited[0][0][0] != 0):
        break
    for i in range(6):
        nx = max(0, x - arr[i][0])
        ny = max(0, y - arr[i][1])
        nz = max(0, z - arr[i][2])
        if visited[nx][ny][nz] == 0:
            visited[nx][ny][nz] = visited[x][y][z] + 1
            dq.append([nx, ny, nz])

print(visited[0][0][0] - 1)