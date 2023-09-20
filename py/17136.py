arr = [list(map(int, input().split())) for _ in range(10)]
p = [0, 5, 5, 5, 5, 5]
answer = int(1e9)

def check(y, x, size):
    if y + size > 10 or x + size > 10:
        return False
    for i in range(y, y + size):
        for j in range(x, x + size):
            if arr[i][j] == 0:
                return False
    return True
        

def draw(y, x, size, v):
    for i in range(y, y + size):
        for j in range(x, x + size):
            arr[i][j] = v


def dfs(y, x, cnt):
    global answer
    if cnt >= answer:
        return
    if x == 10:
        dfs(y + 1, 0, cnt)
        return
    if y == 10:
        answer = min(answer, cnt)
        return
    if arr[y][x] == 0:
        dfs(y, x + 1, cnt)
        return
    
    for i in range(5, 0, -1):
        if p[i] and check(y, x, i):
            p[i] -= 1
            draw(y, x, i, 0)
            dfs(y, x + i, cnt + 1)
            draw(y, x, i, 1)
            p[i] += 1
    return


dfs(0, 0, 0)
print(-1 if answer == int(1e9) else answer)