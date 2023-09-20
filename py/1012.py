t = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(i, j):
    st = [[i, j]]
    visited[i][j] = 1

    while(st):
        y, x = st.pop()
        visited[y][x] = 1

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if(0 <= ny < n and 0 <= nx < m):
                if(arr[ny][nx] == 1 and visited[ny][nx] == 0):
                    st.append([ny, nx])

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    res = 0
    for i in range(n):
        for j in range(m):
            if(arr[i][j] == 1 and visited[i][j] == 0):
                dfs(i, j)
                res += 1;

    print(res)