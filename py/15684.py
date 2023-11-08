import sys
from itertools import combinations
input = sys.stdin.readline

c, k, r = map(int, input().split())
graph = [[0] * c for _ in range(r)]
visited = [[0] * c for _ in range(r)]
ladders = []
ladder = []

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[a-1][b] = -1

for y in range(r):
    for x in range(c - 1):
        if graph[y][x] == 0 and graph[y][x+1] == 0:
            ladders.append([y, x])

def initGame():
    while ladder:
        a, b = ladder.pop()
        graph[a][b] = 0
        graph[a][b + 1] = 0


def startGame():
    for i in range(c):
        x = i
        for step in range(r):
            if graph[step][x] == 1:
                x += 1
            elif graph[step][x] == -1:
                x -= 1
        if x != i:
            return False
    return True


def setGame(cnt):
    for ladderr in combinations(ladders, cnt):
        for a, b in ladderr:
            graph[a][b] = 1
            graph[a][b + 1] = -1
            ladder.append([a, b])

        if startGame():
            return True
        
        initGame()
        
    return False

cnt = 0
while True:
    if cnt > 3:
        print(-1)
        break

    if setGame(cnt):
        print(cnt)
        break

    cnt += 1