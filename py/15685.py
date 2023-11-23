# import sys
# input = sys.stdin.readline

# graph = [[0 for _ in range(101)] for _ in range(101)]
# dy = [0, -1, 0, 1]
# dx = [1, 0, -1, 0]

# n = int(input())
# for _ in range(n):
#     x, y, d, g = map(int, input().split())

#     graph[y][x] = 1
#     route = [d]

#     for i in range(g):
#         temp = []
#         for j in route[::-1]:
#             temp.append((j + 1) % 4)
#         route += temp
    
#     for i in route:
#         y += dy[i]
#         x += dx[i]

#         if 0 <= y <= 100 and 0 <= x <= 100:
#             graph[y][x] = 1

# answer = 0
# for y in range(100):
#     for x in range(100):
#         if graph[y][x]:
#             if graph[y + 1][x] and graph[y][x + 1] and graph[y + 1][x + 1]:
#                 answer += 1

# print(answer)

import sys
from copy import deepcopy
input = sys.stdin.readline

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

n = int(input())
graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon = [d]

    for i in range(g):
        nextDragon = deepcopy(dragon)[::-1]
        
        for j in range(2 ** i):
            nextDragon[j] = (nextDragon[j] + 1) % 4
        
        dragon += nextDragon

    graph[y][x] = 1
    ny, nx = y, x
    for i in dragon:
        ny += dy[i]
        nx += dx[i]
        graph[ny][nx] = 1

answer = 0
for y in range(100):
    for x in range(100):
        if graph[y][x] and graph[y + 1][x] and graph[y][x + 1] and graph[y + 1][x + 1]:
            answer += 1

print(answer)