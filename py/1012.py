# t = int(input())

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def dfs(i, j):
#     st = [[i, j]]
#     visited[i][j] = 1

#     while(st):
#         y, x = st.pop()
#         visited[y][x] = 1

#         for d in range(4):
#             ny = y + dy[d]
#             nx = x + dx[d]

#             if(0 <= ny < n and 0 <= nx < m):
#                 if(arr[ny][nx] == 1 and visited[ny][nx] == 0):
#                     st.append([ny, nx])

# for _ in range(t):
#     m, n, k = map(int, input().split())
#     arr = [[0 for _ in range(m)] for _ in range(n)]
#     visited = [[0 for _ in range(m)] for _ in range(n)]

#     for _ in range(k):
#         x, y = map(int, input().split())
#         arr[y][x] = 1

#     res = 0
#     for i in range(n):
#         for j in range(m):
#             if(arr[i][j] == 1 and visited[i][j] == 0):
#                 dfs(i, j)
#                 res += 1;

#     print(res)




import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    dq = deque([[y, x]])

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < c and 0 <= nx < r:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    dq.append([ny, nx])

tc = int(input())
for _ in range(tc):
    r, c, k = map(int, input().split())

    graph = [[0 for _ in range(r)] for _ in range(c)]
    visited = [[0 for _ in range(r)] for _ in range(c)]
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    answer = 0 
    for y in range(c):
        for x in range(r):
            if graph[y][x] and not visited[y][x]:
                visited[y][x] = 1
                bfs(y, x)
                answer += 1

    print(answer)