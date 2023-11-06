import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [False] * 26

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

visited[ord(graph[0][0]) - 65] = 1
answer = -1

def dfs(y, x, lv):
    global answer
    
    answer = max(answer, lv)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < r and 0 <= nx < c:
            if not visited[ord(graph[ny][nx]) - 65]:
                visited[ord(graph[ny][nx]) - 65] = True
                dfs(ny, nx, lv + 1)
                visited[ord(graph[ny][nx]) - 65] = False

dfs(0, 0, 1)
print(answer)