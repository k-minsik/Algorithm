import sys
input = sys.stdin.readline

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())
graph = [[0] * (C + 1) for _ in range(R + 1)]
sharks = [[]]

def move(r, c, s, d):
    nr, nc = r, c

    for _ in range(s):
        nr += dy[d]
        nc += dx[d]

        if nr < 1 or nr > R or nc < 1 or nc > C:
            if d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 4
            elif d == 4:
                d = 3

            nr += dy[d] * 2
            nc += dx[d] * 2

    return nr, nc, d


for i in range(1, M + 1):
    r, c, s, d, z = map(int, input().split())
    graph[r][c] = i
    sharks.append([i, r, c, s, d, z])

answer = 0
for x in range(1, C + 1):
    for y in range(1, R + 1):
        if graph[y][x]:
            answer += sharks[graph[y][x]][5]
            sharks[graph[y][x]] = []
            graph[y][x] = 0
            break

    newGraph = [[0] * (C + 1) for _ in range(R + 1)]
    for shark in sharks[1:]:
        if shark == []:
            continue

        i, r, c, s, d, z = shark
        nr, nc, nd = move(r, c, s, d)

        if not newGraph[nr][nc] or sharks[newGraph[nr][nc]][5] < z:
                sharks[newGraph[nr][nc]] = []
                newGraph[nr][nc] = i
                sharks[i] = [i, nr, nc, s, nd, z]
            
        else:
            sharks[i] = []

    graph = newGraph

print(answer)