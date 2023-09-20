import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(k):
    a, b = map(int, input().split())
    
    arr[a] += [b]

def dfs(node):
    visited[node] = 1

    for com in arr[node]:
        if not visited[com]:
            dfs(com)

dfs(1)
print(sum(visited) - 1)
print(arr)