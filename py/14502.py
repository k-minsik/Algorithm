# from collections import deque
# from itertools import combinations
# import copy

# n, m = map(int, input().split())
# lab = []
# zero = []
# virus = deque()

# for i in range(n):
#     v = list(map(int, input().split()))
#     lab.append(v)
#     for j in range(len(v)):
#         if v[j] == 2:
#             virus.append([i, j])
#         elif v[j] == 0:
#             zero.append([i, j])

# res = 0
# for z in combinations(zero, 3):
#     lab_tmp = copy.deepcopy(lab)
#     virus_tmp = copy.deepcopy(virus)
#     lab_tmp[z[0][0]][z[0][1]] = 1
#     lab_tmp[z[1][0]][z[1][1]] = 1
#     lab_tmp[z[2][0]][z[2][1]] = 1

#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     while virus_tmp:
#         x, y = virus_tmp.popleft()
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]

#             if 0 <= nx < n and 0 <= ny < m:
#                 if lab_tmp[nx][ny] == 0:
#                     lab_tmp[nx][ny] = 2
#                     virus_tmp.append([nx, ny])

#     cnt = 0
#     for l in lab_tmp:
#         cnt += l.count(0)
    
#     if cnt > res:
#         res = cnt


# print(res)


import sys
from copy import deepcopy
from itertools import combinations
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

c, r = map(int, input().split())
answer = 0
graphInit = []
virusInit = []
zeros = []

for y in range(c):
    row = list(map(int, input().split()))
    graphInit.append(row)

    for x in range(r):
        if row[x] == 0:
            zeros.append([y, x])
        elif row[x] == 2:
            virusInit.append([y, x])

for one, two, three in combinations(zeros, 3):
    graph = deepcopy(graphInit)
    virus = deepcopy(virusInit)

    graph[one[0]][one[1]] = 1
    graph[two[0]][two[1]] = 1
    graph[three[0]][three[1]] = 1

    while virus:
        y, x = virus.pop()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < c and 0 <= nx < r:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 2
                    virus.append([ny, nx])
    
    count = 0
    for y in range(c):
        for x in range(r):
            if graph[y][x] == 0:
                count += 1

    answer = max(answer, count)

print(answer)