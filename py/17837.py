# import sys
# input = sys.stdin.readline

# dy = [0, 0, -1, 1]
# dx = [1, -1, 0, 0]

# n, k = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# move = [[[] for _ in range(n)] for _ in range(n)]
# horse = []

# for i in range(k):
#     y, x, d = map(int, input().split())
#     horse.append([y-1, x-1, d-1])
#     move[y-1][x-1].append(i)

# def solve(i):
#     go = True
#     y, x, d = horse[i]
#     ny = y + dy[d]
#     nx = x + dx[d]

#     if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] != 2:
#         pass
        
#     else:
#         d ^= 1
#         ny = y + dy[d]
#         nx = x + dx[d]
#         horse[i][2] = d

#         if not(0 <= ny < n and 0 <= nx < n) or graph[ny][nx] == 2:
#             go = False
#             ny = y
#             nx = x
    
#     if go:
#         idx = move[y][x].index(i)
#         moving = move[y][x][idx:]
#         move[y][x] = move[y][x][:idx]

#         if graph[ny][nx] == 0:
#                 move[ny][nx].extend(moving)
#         elif graph[ny][nx] == 1:
#                 move[ny][nx].extend(moving[::-1])

#         for j in moving:
#             horse[j] = [ny, nx, horse[j][2]]

#     if len(move[ny][nx])>= 4:
#          return True

#     return False

# cnt = 0
# while True:
#     cnt += 1
#     if cnt > 1000:
#         break
    
#     for i in range(k):
#         flag = solve(i)
#         if flag:
#             print(cnt)
#             exit()

# print(-1)

import sys
input = sys.stdin.readline

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
horse = [[-1, -1, -1]]
horseGraph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(1, k + 1):
    y, x, d = map(int, input().split())
    horse.append([y - 1, x - 1, d - 1])
    horseGraph[y - 1][x - 1].append(i)

answer = 1
while True:
    if answer > 1000:
        break

    for i in range(1, k + 1):
        y, x, d = horse[i]

        ny = y + dy[d]
        nx = x + dx[d]

        if not (0 <= ny < n and 0 <= nx < n) or graph[ny][nx] == 2:
            d ^= 1
            ny = y + dy[d]
            nx = x + dx[d]
            horse[i][2] = d

            if not (0 <= ny < n and 0 <= nx < n) or graph[ny][nx] == 2:
                continue

        idx = horseGraph[y][x].index(i)
        moveHorse = horseGraph[y][x][idx:]
        horseGraph[y][x] = horseGraph[y][x][:idx]

        if graph[ny][nx] == 0:
            horseGraph[ny][nx].extend(moveHorse)
        elif graph[ny][nx] == 1:
            horseGraph[ny][nx].extend(moveHorse[::-1])
        
        if len(horseGraph[ny][nx]) >= 4:
            print(answer)
            exit()

        for h in moveHorse:
            horse[h] = [ny, nx, horse[h][2]]


    answer += 1

print(-1)