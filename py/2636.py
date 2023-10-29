# # import sys
# # input = sys.stdin.readline

# # dy = [-1, 0, 1, 0]
# # dx = [0, 1, 0, -1]

# # n, m = map(int, input().split())
# # arr = [list(map(int, input().split())) for _ in range(n)]

# # def dfs(y, x):
# #     visited[y][x] = 1
# #     if arr[y][x] == 1:
# #         st.append([y, x])
# #         return

# #     for i in range(4):
# #         ny = y + dy[i]
# #         nx = x + dx[i]

# #         if 0 <= ny < n and 0 <= nx < m:
# #             if visited[ny][nx] == 0:
# #                 dfs(ny, nx)
# #     return

# # answer = 0
# # while True:
# #     cnt = 0
# #     visited = [[0 for _ in range(m)] for _ in range(n)]
# #     st = []

# #     dfs(0, 0)

# #     for c in st:
# #         cnt += 1
# #         arr[c[0]][c[1]] = 0

# #     flag = 0
# #     for i in range(n):
# #         for j in range(m):
# #             if arr[i][j] == 1:
# #                 flag = 1

# #     answer += 1
# #     if flag == 0:
# #         break

# # print(answer)
# # print(cnt)

# import sys
# input = sys.stdin.readline

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# def dfs(y, x):
#     st2 = []
#     st2.append([y, x])
#     while(st2):
#         y, x = st2.pop()
#         visited[y][x] = 1

#         if arr[y][x] == 1:
#             st.append([y, x])

#         else:
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]

#                 if 0 <= ny < n and 0 <= nx < m:
#                     if visited[ny][nx] == 0:
#                         st2.append([ny, nx])
#                         visited[ny][nx] = 1

# answer = 0
# while True:
#     cnt = 0
#     visited = [[0 for _ in range(m)] for _ in range(n)]
#     st = []

#     dfs(0, 0)

#     for c in st:
#         cnt += 1
#         arr[c[0]][c[1]] = 0

#     flag = 0
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 1:
#                 flag = 1

#     answer += 1
#     if flag == 0:
#         break

# print(answer)
# print(cnt)


import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

c, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(c)]

def dfs(y, x):
    visited = [[False for _ in range(r)] for _ in range(c)]
    stack = [[y, x]]
    meltCheese = []

    while stack:
        y, x = stack.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < c and 0 <= nx < r and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    stack.append([ny, nx])
                    visited[ny][nx] = True
                else:
                    meltCheese.append([ny, nx])
                    visited[ny][nx] = True
    
    for y, x in meltCheese:
        graph[y][x] = 0

    return len(meltCheese)

def check():
    for y in range(c):
        for x in range(r):
            if graph[y][x] == 1:
                return True
    
    return False


time = 0
while check():
    lastCheese = dfs(0, 0)
    time += 1

print(time)
print(lastCheese)