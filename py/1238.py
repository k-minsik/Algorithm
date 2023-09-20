import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    temp = [int(1e9) for _ in range(n + 1)]
    temp[start] = 0

    while q:
        t, now = heapq.heappop(q)
        if temp[now] < t:
            continue

        for next, fee in graph[now]:
            cost = t + fee
            if cost < temp[next]:
                temp[next] = cost
                heapq.heappush(q, [cost, next])

    return temp

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

ret = [[] for _ in range(n + 1)]
answer = 0 
for i in range(1, n + 1):
    ret[i] = dijkstra(i)

for i in range(1, n + 1):
    answer = max(answer, ret[i][x] + ret[x][i])

print(ret)
print(answer)