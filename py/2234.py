import sys
from collections import deque
input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
rooms = [0]
visited = [[0] * c for _ in range(r)]

roomCount = 0
maxSize = 0
breakSize = 0

def bfs(y, x, roomNum):
    count = 1
    dq = deque([[y, x]])

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            if not graph[y][x] & (1 << i):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < r and 0 <= nx < c:
                    if not visited[ny][nx]:
                        visited[ny][nx] = roomNum
                        dq.append([ny, nx])
                        count += 1
    
    return count

def breakWall():
    global breakSize

    for y in range(r):
        for x in range(c):
            if y < r - 1:
                if visited[y][x] != visited[y + 1][x]:
                    breakSize = max(breakSize, rooms[visited[y][x]] + rooms[visited[y + 1][x]])

            if x < c - 1:
                if visited[y][x] != visited[y][x + 1]:
                    breakSize = max(breakSize, rooms[visited[y][x]] + rooms[visited[y][x + 1]])


roomNum = 1
for y in range(r):
    for x in range(c):
        if not visited[y][x]:
            visited[y][x] = roomNum
            nowSize = bfs(y, x, roomNum)
            maxSize = max(maxSize, nowSize)
            rooms.append(nowSize)
            roomCount += 1
            roomNum += 1

breakWall()

print(roomCount)
print(maxSize)
print(breakSize)