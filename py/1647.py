import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def findParent(child):
    if parent[child] != child:
        parent[child] = findParent(parent[child])
    return parent[child]

def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
graph = []

for _ in range(m):
    s, e, c = map(int, input().split())
    heappush(graph, [c, s, e])

ret = 0
while graph:
    c, s, e = heappop(graph)
    
    if findParent(s) == findParent(e):
        continue

    unionParent(s, e)
    ret += c
    M = c

print(ret - M)