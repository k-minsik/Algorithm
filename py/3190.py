import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
arr = [[0, 0] * n for _ in range(n)]
d = 1
snake = deque([[0, 0]])
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


k = int(input())
for i in range(k):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1


l = int(input())
turn = [0 for _ in range(10001)]
for i in range(l):
    t, c = input().split()
    t = int(t)

    if c == "D":
        turn[t] = 1
    else:
        turn[t] = 3


t = 1
while t < 10001:
    y, x = snake[0]

    ny = y + dy[d]
    nx = x + dx[d]
    if 0 <= ny < n and 0 <= nx < n and [ny, nx] not in snake:
        if arr[ny][nx]:
            arr[ny][nx] = 0
        else:
            snake.pop()
        snake.appendleft([ny, nx])

    else:
        break

    if turn[t]:
        d = (d + turn[t]) % 4

    t += 1


print(t)
