import sys
input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

r, c, m = map(int, input().split())
graph = [[0 for _ in range(c)] for _ in range(r)]

sharks = {}
for i in range(1, m + 1):
    y, x, v, d, lv = map(int, input().split())
    sharks[i] = [r, c, v, d, lv]
    graph[y][x] = i

answer = 0
now = 0
while now < c:
    for i in range(r):
        if graph[i][now] != 0:
            shark = graph[i][now]
            answer += sharks[shark][4]
            sharks.pop(shark)
            break

    for k, v in sharks.items():


