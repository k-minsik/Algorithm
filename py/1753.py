import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = {i : {} for i in range(1, v + 1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

def dijkstra(graph, start):
    distances = {node : int(1e9) for node in graph}
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])

    while q:
        cur_dist, cur_dest = heapq.heappop(q)

        if distances[cur_dest] < cur_dist:
            continue

        for new_dest, new_dist in graph[cur_dest].items():
            distance = cur_dist + new_dist
            if distance < distances[new_dest]:
                distances[new_dest] = distance
                heapq.heappush(q, [distance, new_dest])

    return distances

for k, v in dijkstra(graph, start).items():
    if v == int(1e9):
        print('INF')
        continue

    print(v)