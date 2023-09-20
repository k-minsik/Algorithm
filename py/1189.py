import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
y1, x1, y2, x2 = r-1, 0, 0, c-1

def go(y, x):
    if y == y2 and x == x2:
        if k == visited[y][x]:
            return 1
        else:
            return 0
    
    ret = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if(0 <= ny < r and 0 <= nx < c):
            if(visited[ny][nx] == 0 and arr[ny][nx] != 'T'):
                visited[ny][nx] = visited[y][x] + 1
                ret += go(ny, nx)
                visited[ny][nx] = 0
    return ret

visited[y1][x1] = 1
print(go(y1, x1))