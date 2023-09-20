import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def dfs(now):
    global answer
    visited[now] = True
    team.append(now)
    next = s[now]

    if visited[next]:
        if next in team:
            answer -= (len(team) - team.index(next))
        return
    else:
        dfs(next)


tk = int(input())
for _ in range(tk):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    visited = [True] + [False for _ in range(n)]
    
    answer = n
    for i in range(1, n + 1):
        if not visited[i]:
            team = []
            dfs(i)

    print(answer)