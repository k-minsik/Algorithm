# import sys
# from itertools import permutations
# from collections import deque
# from copy import deepcopy
# input = sys.stdin.readline

# n, m, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# rot = [list(map(int, input().split())) for _ in range(k)]
# answer = int(1e9)

# def rotate(arr, y, x, d):
#     dq = deque()
#     for i in range(x, x + d):
#         dq.append(arr[y][i])
#     for i in range(y + 1, y + d):
#         dq.append(arr[i][x + d - 1])
#     for i in range(x + d - 2, x - 1, -1):
#         dq.append(arr[y + d - 1][i])
#     for i in range(y + d - 2, y, -1):
#         dq.append(arr[i][x])

#     dq.rotate(1)

#     for i in range(x, x + d):
#         arr[y][i] = dq.popleft()
#     for i in range(y + 1, y + d):
#         arr[i][x + d - 1] = dq.popleft()
#     for i in range(x + d - 2, x - 1, -1):
#         arr[y + d - 1][i] = dq.popleft()
#     for i in range(y + d - 2, y, -1):
#         arr[i][x] = dq.popleft()

#     return arr

# for p in permutations(rot, k):
#     temp = deepcopy(arr)
#     for r, c, s in p:
#         y = r - s - 1
#         x = c - s - 1
#         d = 2 * s + 1

#         while d > 0:
#             temp = rotate(temp, y, x, d)
#             y += 1
#             x += 1
#             d -= 2
            
#     for i in temp:
#         answer = min(answer, sum(i))

# print(answer)


import sys
from collections import deque
from itertools import permutations
from copy import deepcopy
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
infos = [list(map(int, input().split())) for _ in range(k)]

answer = 1e9
for info in permutations(infos, k):
    tempGraph = deepcopy(graph)
                         
    for y, x, s in info:
        y -= 1
        x -= 1
        dq = deque([])

        for i in range(1, s + 1):
            for j in range(2 * i + 1):
                dq.append(tempGraph[y - i][x - i + j])
            for j in range(1, 2 * i + 1):
                dq.append(tempGraph[y - i + j][x + i])
            for j in range(1, 2 * i + 1):
                dq.append(tempGraph[y + i][x + i -j])
            for j in range(1, 2 * i):
                dq.append(tempGraph[y + i - j][x - i])
            
            dq.rotate(1)

            for j in range(2 * i + 1):
                tempGraph[y - i][x - i + j] = dq.popleft()
            for j in range(1, 2 * i + 1):
                tempGraph[y - i + j][x + i] = dq.popleft()
            for j in range(1, 2 * i + 1):
                tempGraph[y + i][x + i -j] = dq.popleft()
            for j in range(1, 2 * i):
                tempGraph[y + i - j][x - i] = dq.popleft()

    tempAnswer = 1e9
    for row in range(r):
        tempAnswer = min(tempAnswer, sum(tempGraph[row]))

    answer = min(answer, tempAnswer)
            
print(answer)