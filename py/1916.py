import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [int(1e9)] * (n + 1)

for _ in range(m):
    a, b, p = map(int, input().split())
    arr[a].append([p, b])

start, goal = map(int, input().split())

def dijkstra(s):
    q = []
    heappush(q, (0, s))
    visited[s] = 0

    while q:
        cur_cost, now = heappop(q)

        if visited[now] < cur_cost:
            continue
        else:
            for cost, next in arr[now]:
                next_cost = cur_cost + cost

                if visited[next] > next_cost:
                    heappush(q, (next_cost, next))
                    visited[next] = next_cost

dijkstra(start)
print(visited[goal])