# import sys
# from collections import deque
# input = sys.stdin.readline


# n = int(input())
# arr = [[0, 0] * n for _ in range(n)]
# d = 1
# snake = deque([[0, 0]])
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]


# k = int(input())
# for i in range(k):
#     y, x = map(int, input().split())
#     arr[y-1][x-1] = 1


# l = int(input())
# turn = [0 for _ in range(10001)]
# for i in range(l):
#     t, c = input().split()
#     t = int(t)

#     if c == "D":
#         turn[t] = 1
#     else:
#         turn[t] = 3


# t = 1
# while t < 10001:
#     y, x = snake[0]

#     ny = y + dy[d]
#     nx = x + dx[d]
#     if 0 <= ny < n and 0 <= nx < n and [ny, nx] not in snake:
#         if arr[ny][nx]:
#             arr[ny][nx] = 0
#         else:
#             snake.pop()
#         snake.appendleft([ny, nx])

#     else:
#         break

#     if turn[t]:
#         d = (d + turn[t]) % 4

#     t += 1


# print(t)


import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [[0] * (n + 1) for _ in range(n + 1)]
turn = [0] * 10001
snake = deque([[1, 1]])
visited[1][1] = 1

k = int(input())
for _ in range(k):
    y, x = map(int, input().split())
    graph[y][x] = 1

l = int(input())
for _ in range(l):
    t, c = input().split()
    turn[int(t)] = 1 if c == 'D' else 3

answer, i = 1, 1
while True:
    y, x = snake[0]
    
    ny = y + dy[i]
    nx = x + dx[i]

    if not (0 < ny <= n and 0 < nx <= n) or visited[ny][nx]:
        break

    if graph[ny][nx]:
        graph[ny][nx] = 0
    else:
        py, px = snake.pop()
        visited[py][px] = 0
    
    snake.appendleft([ny, nx])
    visited[ny][nx] = 1
            
    i = (i + turn[answer]) % 4
    answer += 1

print(answer)