import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dq = deque()
dq.append([0, 0])

while dq:
    y, x = dq.popleft()
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if graph[ny][nx] == 1:
                dq.append([ny, nx])
                graph[ny][nx] += graph[y][x]

print(graph[-1][-1])



