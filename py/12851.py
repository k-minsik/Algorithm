import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
size = max(n, k)
graph = [0 for _ in range(2 * size + 1)]
count = [0 for _ in range(2 * size + 1)]
graph[n] = 1
count[n] = 1
dq = deque([n])

while dq:
    x = dq.popleft()

    for nx in [x - 1, x + 1, x * 2]:
        if 0 <= nx < 2 * size + 1:
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                count[nx] += count[x]
                dq.append(nx)
                
            elif graph[nx] == graph[x] + 1:
                count[nx] += count[x]

print(graph[k] - 1)
print(count[k])