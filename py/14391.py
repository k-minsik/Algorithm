# n, m = map(int, input().split())
# arr = [list(input()) for _ in range(n)]

# answer = 0
# for i in range(1 << (n * m)):
#     temp = 0
#     for y in range(n):
#         cur = 0
#         for x in range(m):
#             if (i & (1 << (y * m) + x)) == 0:
#                 cur = cur * 10 + int(arr[y][x])
#             else:
#                 temp += cur
#                 cur = 0
    
#         temp += cur

#     for x in range(m):
#         cur = 0
#         for y in range(n):
#             if (i & (1 << (y * m) + x)) != 0:
#                 cur = cur * 10 + int(arr[y][x])
#             else:
#                 temp += cur
#                 cur = 0
    
#         temp += cur
    
#     answer = max(answer, temp)

# print(answer)


import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(r)]

answer = 0
for i in range(1 << (r * c)):
    visited = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if i & (1 << y * c + x):
                visited[y][x] = 1

    tempAnswer = 0
    # visited = 1 가로
    for y in range(r):
        cur = 0
        for x in range(c):
            if visited[y][x] == 1:
                cur = cur * 10 + graph[y][x]
            else:
                tempAnswer += cur
                cur = 0
        tempAnswer += cur

    # visited = 0 세로
    for x in range(c):
        cur = 0
        for y in range(r):
            if visited[y][x] == 0:
                cur = cur * 10 + graph[y][x]
            else:
                tempAnswer += cur
                cur = 0
        tempAnswer += cur

    answer = max(answer, tempAnswer)

print(answer)