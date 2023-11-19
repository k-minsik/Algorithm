# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# r, c, t = map(int, input().split())
# arr = []
# air = []
# for i in range(r):
#     temp = list(map(int, input().split()))
#     if -1 in temp:
#         air.append([i, temp.index(-1)])
#     arr.append(temp)

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def spread(arr):
#     temp = [[0 for _ in range(c)] for _ in range(r)]
#     for y in range(r):
#         for x in range(c):
#             cnt = 0
#             for i in range(4):
#                 ny = y + dy[i]
#                 nx = x + dx[i]

#                 if 0 <= ny < r and 0 <= nx < c and arr[ny][nx] != -1:
#                     temp[ny][nx] += int(arr[y][x] / 5)
#                     cnt += 1
#             temp[y][x] += arr[y][x] - int(arr[y][x] / 5) * cnt
#     return temp

# def rotate(arr):
#     temp = deepcopy(arr)

#     y, x = air[0]
#     temp[y][1] = 0
#     for i in range(2, c):
#         temp[y][i] = arr[y][i - 1]
    
#     for i in range(y-1, -1, -1):
#         temp[i][c-1] = arr[i + 1][c-1]
    
#     for i in range(c-2, -1, -1):
#         temp[0][i] = arr[0][i + 1]

#     for i in range(1, y):
#         temp[i][0] = arr[i - 1][0]


#     y, x = air[1]
#     temp[y][1] = 0
#     for i in range(2, c):
#         temp[y][i] = arr[y][i - 1]

#     for i in range(y+1, r):
#         temp[i][c-1] = arr[i - 1][c-1]

#     for i in range(c-2, -1, -1):
#         temp[r-1][i] = arr[r-1][i + 1]

#     for i in range(r-2, y, -1):
#         temp[i][0] = arr[i + 1][0]

#     return temp

# answer = 2
# for _ in range(t):
#     arr = spread(arr)
#     arr = rotate(arr)

# for i in arr:
#     answer += sum(i)
# print(answer)

import sys
from copy import deepcopy
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r, c, t = map(int, input().split())
airCleaner = []
graph = []
for y in range(r):
    row = list(map(int, input().split()))
    for x in range(c):
        if row[x] == -1:
            airCleaner.append([y, x])
    graph.append(row)


def spreadDusty():
    spreadGraph = [[0] * c for _ in range(r)]

    for y in range(r):
        for x in range(c):
            if graph[y][x] != -1:
                count = 0

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != -1:
                        spreadGraph[ny][nx] += graph[y][x] // 5
                        count += 1

                spreadGraph[y][x] += graph[y][x] - (graph[y][x] // 5) * count
            
            else:
                spreadGraph[y][x] = -1

    return spreadGraph

def onCleaner():
    cleanGraph = deepcopy(graph)

    y, x = airCleaner[0]
    cleanGraph[y][1] = 0
    for i in range(2, c):
        cleanGraph[y][i] = graph[y][i - 1]

    for i in range(y):
        cleanGraph[i][c - 1] = graph[i + 1][c - 1]

    for i in range(c - 1):
        cleanGraph[0][i] = graph[0][i + 1]

    for i in range(1, y):
        cleanGraph[i][0] = graph[i - 1][0]


    y, x = airCleaner[1]
    cleanGraph[y][1] = 0
    for i in range(2, c):
        cleanGraph[y][i] = graph[y][i - 1]
    
    for i in range(y + 1, r):
        cleanGraph[i][c - 1] = graph[i - 1][c - 1]

    for i in range(c - 1):
        cleanGraph[r - 1][i] = graph[r - 1][i + 1]

    for i in range(y + 1, r - 1):
        cleanGraph[i][0] = graph[i + 1][0]

    return cleanGraph

for _ in range(t):
    graph = spreadDusty()
    graph = onCleaner()

answer = 2
for i in graph:
    answer += sum(i)
print(answer)