import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
water, nextWater, swan, nextSwan = deque(), deque(), deque(), deque()

for y in range(r):
    for x in range(c):
        if graph[y][x] == 'L':
            swanY, swanX = y, x
        if graph[y][x] != 'X':
            water.append([y, x])

swan.append([swanY, swanX])
visited[swanY][swanX] = True

def WaterMelting():
    while water:
        y, x = water.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if graph[ny][nx] == 'X':
                    nextWater.append([ny, nx])
                    graph[ny][nx] = '.'

def MoveSwan():
    while swan:
        y, x = swan.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == '.':
                    swan.append([ny, nx])
                elif graph[ny][nx] == 'X':
                    nextSwan.append([ny, nx])
                elif graph[ny][nx] == 'L':
                    return True
                
    return False

answer = 0
while True:
    if MoveSwan():
        break
    
    WaterMelting()
    water, nextWater = nextWater, deque()
    swan, nextSwan = nextSwan, deque()

    answer += 1

print(answer)