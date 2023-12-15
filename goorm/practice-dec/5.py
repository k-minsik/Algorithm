import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = [0] * 11

def bfs(y, x):
    num = graph[y][x]
    count = 1
    dq = deque([[y, x]])
    visited[y][x] = True

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == num and not visited[ny][nx]:
                    count += 1
                    visited[ny][nx] = True
                    dq.append([ny, nx])
    
    answer[num] = max(answer[num], count)

for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            bfs(y, x)

print(*answer[1:])