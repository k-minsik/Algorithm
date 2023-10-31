# import sys
# from collections import deque
# input = sys.stdin.readline

# arr = [[9, 3, 1], [9, 1, 3], 
# [3, 9, 1], [3, 1, 9], 
# [1, 9, 3], [1, 3, 9]]

# n = int(input())
# scv = list(map(int, input().split()))
# for _ in range(3-n):
#     scv.append(0)
# visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
# dq = deque()

# dq.append(scv)
# visited[scv[0]][scv[1]][scv[2]] = 1

# while dq:
#     x, y, z = dq.popleft()
#     if(visited[0][0][0] != 0):
#         break
#     for i in range(6):
#         nx = max(0, x - arr[i][0])
#         ny = max(0, y - arr[i][1])
#         nz = max(0, z - arr[i][2])
#         if visited[nx][ny][nz] == 0:
#             visited[nx][ny][nz] = visited[x][y][z] + 1
#             dq.append([nx, ny, nz])

# print(visited[0][0][0] - 1)


import sys
from collections import deque
input = sys.stdin.readline

attack = [[9, 3, 1], [9, 1, 3], [3, 9, 1], [3, 1, 9], [1, 9, 3], [1, 3, 9]]

n = int(input())
hp = (list(map(int, input().split())) + [0, 0])[:3]
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dq = deque([hp])

while dq:
    one, two, three = dq.popleft()

    if one == 0 and two == 0 and three == 0:
        print(visited[one][two][three])
        break

    for i in range(6):
        four = max(0, one - attack[i][0])
        five = max(0, two - attack[i][1])
        six = max(0, three - attack[i][2])

        if visited[four][five][six] == 0:
            visited[four][five][six] = visited[one][two][three] + 1
            dq.append([four, five, six])