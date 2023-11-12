# import sys
# input = sys.stdin.readline

# def dfs(node, visited):
#     visited[node] = 1
#     for next in arr[node]:
#         if not visited[next]:
#             visited = dfs(next, visited)
#     return visited

# for _ in range(int(input())):
#     n = int(input())
#     e = int(input())
#     arr = [[] for _ in range(n + 1)]

#     for _ in range(e):
#         a, b = map(int, input().split())
#         arr[a].append(b)
#         arr[b].append(a)

#     if n != e + 1:
#         print("graph")
#         continue
    
#     visited = [False for _ in range(n + 1)]
#     visited[0] = True
#     dfs(1, visited)

#     if False in visited:
#         print("graph")
#     else:
#         print("tree")


import sys
input = sys.stdin.readline

def dfs(idx):
    visited[idx] = True

    for next in adjList[idx]:
        if not visited[next]:
            dfs(next)

tc = int(input())
for _ in range(tc):
    n = int(input())
    m = int(input())
    adjList = [[] for _ in range(n)]
    visited = [False] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1

        adjList[a].append(b)
        adjList[b].append(a)

    check = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            check += 1

    if check == 1 and m == n - 1:
        print("tree")
    else:
        print("graph")