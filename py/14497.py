# import sys
# from collections import deque
# input = sys.stdin.readline

# n, m = map(int, input().split())
# a, b, c, d = map(int, input().split())
# a, b, c, d = a-1, b-1, c-1, d-1
# arr = [list(input().rstrip()) for _ in range(n)]

# answer = 0
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# dq = deque()
# while True:
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#     visited[a][b] = 1
#     answer += 1
#     dq.append([a, b])
#     while dq:
#         y, x = dq.popleft()

#         if y == c and x == d:
#             break

#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
#                 if arr[ny][nx] == '#':
#                     visited[ny][nx] = 1
#                     dq.append([ny, nx])
#                     break
#                 elif arr[ny][nx] == '1':
#                     visited[ny][nx] = 1
#                     arr[ny][nx] = '0'
#                 elif arr[ny][nx] == '0':
#                     visited[ny][nx] = 1
#                     dq.append([ny, nx])

#     if y == c and x == d:
#         break

# print(answer)


import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c = map(int, input().split())
y1, x1, y2, x2 = map(int, input().split())
y1, x1, y2, x2 = y1-1, x1-1, y2-1, x2-1
graph = [list(input().rstrip()) for _ in range(r)]

catch = False
answer = 0 
while not catch:
    answer += 1
    visited = [[0 for _ in range(c)] for _ in range(r)]
    visited[y1][x1] = 1
    dq = deque([[y1, x1]])

    while dq and not catch:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if graph[ny][nx] == '1':
                    visited[ny][nx] = 1
                    graph[ny][nx] = '0'

                elif graph[ny][nx] == '0':
                    visited[ny][nx] = 1
                    dq.append([ny, nx])

                elif graph[ny][nx] == '#':
                    catch = True
                    break

print(answer)