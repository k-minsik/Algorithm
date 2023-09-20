h, w = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(h)]
answer = [[-1 for _ in range(w)] for _ in range(h)]

def mv(i, j):
    while True:
        j += 1
        if j == w:
            break
        if answer[i][j] == 0:
            break
        elif answer[i][j] == -1:
            answer[i][j] = answer[i][j-1] + 1

for i in range(h):
    for j in range(w-1, -1, -1):
        if arr[i][j] == 'c':
            answer[i][j] = 0
            mv(i, j)

for i in range(h):
    for j in range(w):
        print(answer[i][j], end = ' ')
    print()
