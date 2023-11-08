import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graphRow = [list(map(int, input().split())) for _ in range(n)]
graphCol = [list(i) for i in zip(*graphRow)]

def check(row):
    visited = [0] * n
    
    for x in range(n - 1):
        nx = x + 1
        if row[x] == row[nx]:
            continue

        elif row[x] == row[nx] - 1:
            if nx - l < 0:
                return 0
            for i in range(1, l + 1):
                if visited[nx - i]:
                    return 0
                visited[nx - i] = 1

        elif row[x] == row[nx] + 1:
            if x + l > n - 1:
                return 0
            for i in range(1, l + 1):
                if visited[x + i]:
                    return 0
                visited[x + i] = 1
        else:
            return 0

    return 1

answer = 0
for i in range(n):
    answer += check(graphRow[i])
    answer += check(graphCol[i])

print(answer)