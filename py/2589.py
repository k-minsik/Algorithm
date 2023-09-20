import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, d):
    dq = deque()
    dis = [0]
    visited[y][x] = 1
    dq.append([y, x, d])

    while dq:
        y, x, d = dq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 'L' and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    dis.append(d+1)
                    dq.append([ny, nx, d + 1])
    
    return max(dis)

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[0 for _ in range(m)] for _ in range(n)]
            answer = max(answer, bfs(i, j, 0))

print(answer)