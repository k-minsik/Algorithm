import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = {i : [] for i in range(1, n + 1)}
degree = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    data[s].append(e)
    degree[e] += 1

dq = deque()
for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)

answer = []
while dq:
    now = dq.popleft()

    for next in data[now]:
        degree[next] -= 1

        if degree[next] == 0:
            dq.append(next)

    answer.append(now)

for i in answer:
    print(i, end = ' ')