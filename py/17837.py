import sys
input = sys.stdin.readline

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

n, k =  map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mal = [list(map(int, input().split())) for _ in range(k)]
graph = [[[] for _ in range(n)] for _ in range(n)]

ret = 0
while ret < 1001:
    ret += 1
    flag = 0
    for i in range(k):
        y, x, d = mal[i]

        ny, nx = y + dy[d], x + dx[d]

        if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] != 2:
            pass

        else:
            ny, nx = y - dy[d], x - dx[d]
        





        if len(graph[ny][nx]) == 4:
            flag = 1
            break

    if flag:
        break

    
print(ret if ret <= 1000 else -1)