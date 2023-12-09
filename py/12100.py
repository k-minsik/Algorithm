# import sys
# from copy import deepcopy
# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# answer = 0

# def rotate(arr):   # 시계 방향
#     temp = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             temp[i][j] = arr[n - j - 1][i]

#     return temp

# def move(arr, d):  # 왼쪽으로 밀기
#     temp = deepcopy(arr)
#     for _ in range(d):
#         temp = rotate(temp)

#     for i in range(n):
#         here = 0
#         for j in range(1, n):
#             if temp[i][j]:
#                 tmp = temp[i][j]
#                 temp[i][j] = 0
#                 if temp[i][here] == 0:
#                     temp[i][here] = tmp
#                 elif temp[i][here] == tmp:
#                     temp[i][here] = tmp * 2
#                     here += 1
#                 else:
#                     here += 1
#                     temp[i][here] = tmp

#     return temp


# def dfs(arr, cnt):
#     global answer
#     if cnt == 5:
#         for i in range(n):
#             for j in range(n):
#                 answer = max(answer, arr[i][j])
#         return
    
#     for i in range(4): # 왼 아 오 위
#         temp = move(arr, i)
#         dfs(temp, cnt + 1)

# dfs(arr, 0)
# print(answer)

import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate(graph):
    rotateGraph = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            rotateGraph[y][x] = graph[n - x - 1][y]

    return rotateGraph

def move(d):
    rotateGraph = deepcopy(graph)
    for _ in range(d):
        rotateGraph = rotate(rotateGraph)

    for y in range(n):
        here = 0
        for x in range(1, n):
            if rotateGraph[y][x]:
                tmp = rotateGraph[y][x]
                rotateGraph[y][x] = 0
                if rotateGraph[y][here] == 0:
                    rotateGraph[y][here] = tmp
                elif rotateGraph[y][here] == tmp:
                    rotateGraph[y][here] = tmp * 2
                    here += 1
                else:
                    here += 1
                    rotateGraph[y][here] = tmp

    return rotateGraph


def dfs(depth, graph):
    global answer
    if depth == 5:
        for y in range(n):
            for x in range(n):
                answer = max(answer, graph[y][x])
        return
    
    for i in range(4):
        newGraph = move(i)
        dfs(depth + 1, newGraph)

answer = 0
dfs(0, graph)
print(answer)