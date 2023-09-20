import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)] 

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(node):
    for i in range(1, n+1):
        if arr[node][i]:
            now = i

            if not visited[now]:
                visited[now] = 1
                dfs(now)


cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = 1
        dfs(i)
        cnt += 1

print(cnt)