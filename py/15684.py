import sys
input = sys.stdin.readline
ret = 1e9

n, m, h = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    y, x = map(int, input().split())
    y, x = y-1, x-1
    arr[y][x] = 1
    arr[y][x+1] = -1

def check():
    for start in range(n):
        s = start
        for step in range(h):
            if arr[step][s] == 1:
                s += 1
            elif arr[step][s] == -1:
                s -= 1
        if s != start:
            return False
    return True

def do(now, cnt):
    global ret
    if cnt > 3 or cnt >= ret:
        return
    if check() == True:
        ret = min(ret, cnt)
        return
        
    for i in range(now, h):
        for j in range(n-1):
            if arr[i][j] == 0 and arr[i][j+1] == 0:
                arr[i][j] = 1
                arr[i][j+1] = -1
                do(i, cnt + 1)
                arr[i][j] = 0
                arr[i][j+1] = 0

do(0, 0)

print(ret) if ret <= 3 else print(-1)