import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
price = [[0] * (n-2) for _ in range(n - 2)]
visited = [[0] * (n-2) for _ in range(n - 2)]
answer = int(1e9)
fee = 0

for y in range(1, n - 1):
    for x in range(1, n - 1):
        price[y - 1][x - 1] = graph[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            price[y - 1][x - 1] += graph[ny][nx]

def check(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n - 2 and 0 <= nx < n - 2:
            if visited[ny][nx]:
                return False
            
    return True

def dfs(cnt):
    global answer, fee

    if cnt == 3:
        answer = min(answer, fee)
        return
    
    for y in range(n - 2):
        for x in range(n - 2):
            if not visited[y][x] and check(y, x):
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n - 2 and 0 <= nx < n - 2:
                        visited[ny][nx] = 1
                fee += price[y][x]

                dfs(cnt + 1)

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < n - 2 and 0 <= nx < n - 2:
                        visited[ny][nx] = 0
                fee -= price[y][x]

dfs(0)
print(answer)