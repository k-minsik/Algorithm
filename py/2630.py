import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
w, b = 0, 0

def go(y, x, N):
    global w, b
    c = arr[y][x]

    for i in range(y, y + N):
        for j in range(x, x + N):
            if arr[i][j] != c:
                go(y, x, N//2)
                go(y, x + N//2, N//2)
                go(y+ N//2, x, N//2)
                go(y+ N//2, x+ N//2, N//2)
                return

    if c:
        b += 1
    else:
        w += 1

go(0, 0, n)
print(w)
print(b)

