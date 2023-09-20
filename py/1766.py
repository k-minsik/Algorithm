from sys import stdin
from collections import deque
import heapq
input = stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
degree = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    degree[e] += 1

hq = []
for i in range(1, n + 1):
    if degree[i] == 0:
        heapq.heappush(hq, i)

answer = []
while hq:
    now = heapq.heappop(hq)
    answer.append(now)

    for next in graph[now]:
        degree[next] -= 1

        if degree[next] == 0:
            heapq.heappush(hq, next)

print(*answer)