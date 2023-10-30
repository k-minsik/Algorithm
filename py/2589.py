# import sys
# from collections import deque
# input = sys.stdin.readline

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def bfs(y, x, d):
#     dq = deque()
#     dis = [0]
#     visited[y][x] = 1
#     dq.append([y, x, d])

#     while dq:
#         y, x, d = dq.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if 0 <= ny < n and 0 <= nx < m:
#                 if arr[ny][nx] == 'L' and not visited[ny][nx]:
#                     visited[ny][nx] = 1
#                     dis.append(d+1)
#                     dq.append([ny, nx, d + 1])
    
#     return max(dis)

# n, m = map(int, input().split())
# arr = [list(input().rstrip()) for _ in range(n)]
# answer = 0

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] == 'L':
#             visited = [[0 for _ in range(m)] for _ in range(n)]
#             answer = max(answer, bfs(i, j, 0))

# print(answer)

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

c, r = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(c)]

def bfs(y, x):
    visited = [[-1 for _ in range(r)] for _ in range(c)]
    dq = deque([[y, x]])
    visited[y][x] = 0

    dist = 0
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < c and 0 <= nx < r:
                if graph[ny][nx] == 'L' and visited[ny][nx] == -1:
                    dq.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
                    dist = max(dist, visited[ny][nx])

    return dist


answer = 0
for y in range(c):
    for x in range(r):
        if graph[y][x] == 'L':
            answer = max(answer, bfs(y, x))

print(answer)