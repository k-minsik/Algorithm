import sys, heapq
input = sys.stdin.readline

def findParent(node):
    if parent[node] == node:
        return node
    parent[node] = findParent(parent[node])
    return parent[node]


v, e = map(int, input().split())
graph = []
parent = [i for i in range(v + 1)]

for i in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(graph, [c, a, b])

ret = 0
while graph:
    c, a, b = heapq.heappop(graph)
    Pa, Pb = findParent(a), findParent(b)
    if Pa == Pb:
        continue

    if Pa < Pb:
        parent[Pb] = Pa
    else:
        parent[Pa] = Pb
    ret += c

print(ret)