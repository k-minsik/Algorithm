# n = int(input())
# arr = []

# m, M = 1e9, -1e9
# res = 0
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def dfs(y, x, h):
#     st = []
#     st.append([y, x])

#     while st:
#         y, x = st.pop()
#         visited[y][x] = 1

#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]

#             if 0 <= ny < n and 0 <= nx < n:
#                 if arr[ny][nx] > h and visited[ny][nx] == 0:
#                     st.append([ny, nx])

# for _ in range(n):
#     temp = list(map(int, input().split()))
#     M = max(M, max(temp))
#     m = min(m, min(temp))
#     arr.append(temp)
    
# for h in range(m-1, M):
#     res2 = 0
#     visited = [[0 for _ in range(n)] for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] > h and visited[i][j] == 0:
#                 dfs(i, j, h)
#                 res2 += 1

#     res = max(res, res2)

# print(res)

import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x, h):
    dq = deque([[y, x]])

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] > h and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    dq.append([ny, nx])

low, high = 200, 0
n = int(input())
graph = []

for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    low = min(low, min(row)) - 1
    high = max(high, max(row))

answer = 0 
while True:
    count = 0
    if low >= high:
        break

    visited = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if graph[y][x] > low and not visited[y][x]:
                visited[y][x] = 1
                bfs(y, x, low)
                count += 1

    answer = max(answer, count)
    low += 1

print(answer)

