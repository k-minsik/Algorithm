import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, d = map(int, input().split())
# d = 0 : 북, 1 : 동, 2 : 남, 3 : 서
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
while True:
    if arr[y][x] == 0 and not visited[y][x]:
        answer += 1
        visited[y][x] = 1
    
    trash = 0
    for i in range(4):
        d = (d + 3) % 4
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    trash = 1
                    y, x = ny, nx
                    break

            
    if not trash:
        ny = y - dy[d]
        nx = x - dx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1:
                break
            else:
                y, x = ny, nx

print(answer)