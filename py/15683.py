import sys
from copy import deepcopy
input = sys.stdin.readline

def scan(idx, dir):
    rollback = []
    y, x = cctv[idx]

    if graph[y][x] == 1:
        ny, nx = y, x
        while True:
            ny += dy[dir]
            nx += dx[dir]

            if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 6:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = -1
                    rollback.append([ny, nx])
            
            else:
                break

    elif graph[y][x] == 2:
        for i in range(2):
            ny, nx = y, x

            while True:
                ny += dy[(dir + i * 2) % 4]
                nx += dx[(dir + i * 2) % 4]

                if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 6:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = -1
                        rollback.append([ny, nx])
                
                else:
                    break

    elif graph[y][x] == 3:
        for i in range(2):
            ny, nx = y, x

            while True:
                ny += dy[(dir + i) % 4]
                nx += dx[(dir + i) % 4]

                if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 6:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = -1
                        rollback.append([ny, nx])
                
                else:
                    break

    elif graph[y][x] == 4:
        for i in range(3):
            ny, nx = y, x

            while True:
                ny += dy[(dir + i) % 4]
                nx += dx[(dir + i) % 4]

                if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 6:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = -1
                        rollback.append([ny, nx])
                
                else:
                    break

    elif graph[y][x] == 5:
        for i in range(4):
            ny, nx = y, x

            while True:
                ny += dy[(dir + i) % 4]
                nx += dx[(dir + i) % 4]

                if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] != 6:
                    if graph[ny][nx] == 0:
                        graph[ny][nx] = -1
                        rollback.append([ny, nx])
                
                else:
                    break

    return rollback


def dfs(lv):
    global answer

    if lv == len(cctv):
        tempAnswer = 0
        for i in range(r):
            for j in range(c):
                if graph[i][j] == 0:
                    tempAnswer += 1
        
        answer = min(answer, tempAnswer)
        return 
    
    for i in range(4):
        rollback = scan(lv, i)
        dfs(lv + 1)

        for y, x in rollback:
            graph[y][x] = 0
    


if __name__ == "__main__":

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    r, c = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(r)] 
    cctv = []
    answer = 64

    for y in range(r):
        for x in range(c):
            if 1 <= graph[y][x] <= 5:
                cctv.append([y, x])

    dfs(0)
    print(answer)