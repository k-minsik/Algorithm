# from collections import deque
# n, k = map(int, input().split())
# arr = [0] * 222222
# visited = [0] * 222222
# record = []

# visited[n] = 1

# dq = deque()
# dq.append(n)

# dx = [[1, 1], [1, -1], [2, 0]]

# while dq:
#     now = dq.popleft()

#     if now == k:
#         answer = visited[now]
#         break

#     for i in range(3):
#         next = now * dx[i][0] + dx[i][1]
#         if 0 <= next <= 200001:
#             if visited[next] == 0:
#                 visited[next] = visited[now] + 1
#                 dq.append(next)
#                 arr[next] = now

# now = k
# record.append(k)

# while now != n:
#     now = arr[now]
#     record.append(now)

# print(visited[k] - 1)
# for i in record[::-1]:
#     print(i, end = " ")

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
size = max(n, k)
graph = [0 for _ in range(2 * size + 1)]
trace = [0 for _ in range(2 * size + 1)]
graph[n] = 1
trace[n] = -1
dq = deque([n])

while dq:
    x = dq.popleft()

    if x == k:
        break

    for nx in [x - 1, x + 1, x * 2]:
        if 0 <= nx < 2 * size + 1:
            if graph[nx] == 0:
                graph[nx] = graph[x] + 1
                trace[nx] = x
                dq.append(nx)

answer = [k]
while True:
    bx = trace[answer[-1]]

    if bx == -1:
        break

    answer.append(bx)


print(graph[k] - 1)
print(*answer[::-1])
    