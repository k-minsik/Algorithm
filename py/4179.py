import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = []
visitedMan = [[0 for _ in range(c)] for _ in range(r)]
visitedFire = [[int(1e9) for _ in range(c)] for _ in range(r)]
qMan = deque([])
qFire = deque([])


for y in range(r):
    row = list(input().rstrip())
    graph.append(row)
    for x in range(c):
        if row[x] == 'J':
            qMan.append([y, x])
            visitedMan[y][x] = 1
        elif row[x] == 'F':
            qFire.append([y, x])
            visitedFire[y][x] = 1

while qFire:
    y, x = qFire.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c:
            if visitedFire[y][x] + 1 < visitedFire[ny][nx]  and graph[ny][nx] != '#':
                visitedFire[ny][nx] = visitedFire[y][x] + 1
                qFire.append([ny, nx])

answer = 0
while qMan:
    y, x = qMan.popleft()
    if y == 0 or y == r - 1 or x == 0 or x == c - 1:
        answer = visitedMan[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if not visitedMan[ny][nx] and graph[ny][nx] != '#':
                if visitedMan[y][x] + 1 < visitedFire[ny][nx]:
                    visitedMan[ny][nx] = visitedMan[y][x] + 1
                    qMan.append([ny, nx])

for i in visitedFire:
    print(i)
print(answer) if answer else print("IMPOSSIBLE")
for i in visitedMan:
    print(i)
