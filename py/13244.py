import sys
input = sys.stdin.readline

def dfs(node, visited):
    visited[node] = 1
    for next in arr[node]:
        if not visited[next]:
            visited = dfs(next, visited)
    return visited

for _ in range(int(input())):
    n = int(input())
    e = int(input())
    arr = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    if n != e + 1:
        print("graph")
        continue
    
    visited = [False for _ in range(n + 1)]
    visited[0] = True
    dfs(1, visited)

    if False in visited:
        print("graph")
    else:
        print("tree")