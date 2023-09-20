m, n, k = map(int, input().split())
arr = [[1 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, s):
    st = []
    st.append([y, x])
    while st:
        s += 1
        y, x= st.pop()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 1 and visited[ny][nx] == 0:
                    st.append([ny, nx])
                    visited[ny][nx] = 1
    return s

for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = 0

cnt = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            s = 0
            visited[i][j] = 1
            s = dfs(i, j, s)
            cnt.append(s)

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i], end = ' ')


