n = int(input())
arr = []

m, M = 1e9, -1e9
res = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, h):
    st = []
    st.append([y, x])

    while st:
        y, x = st.pop()
        visited[y][x] = 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < n:
                if arr[ny][nx] > h and visited[ny][nx] == 0:
                    st.append([ny, nx])

for _ in range(n):
    temp = list(map(int, input().split()))
    M = max(M, max(temp))
    m = min(m, min(temp))
    arr.append(temp)
    
for h in range(m-1, M):
    res2 = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] > h and visited[i][j] == 0:
                dfs(i, j, h)
                res2 += 1

    res = max(res, res2)

print(res)