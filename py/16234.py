import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(y, x):
    world = [[y, x]]
    dq = deque([[y, x]])
    visited[y][x] = True

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and l <= abs(graph[y][x] - graph[ny][nx]) <= r:
                    visited[ny][nx] = True
                    world.append([ny, nx])
                    dq.append([ny, nx])

    return world

answer = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    openWorld = []

    for y in range(n):
        for x in range(n):
            world = bfs(y, x)

            if len(world) > 1:
                openWorld.append(world)

    if len(openWorld) >= 1:
        for worlds in openWorld:
            count = 0
            for w in worlds:
                count += graph[w[0]][w[1]]
            for w in worlds:
                graph[w[0]][w[1]] = count // len(worlds)

    if len(openWorld) == 0:
        break
    
    answer += 1

print(answer)