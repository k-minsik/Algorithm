import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
order = [list(map(int, input().split()))[1:] for _ in range(m)]

answer = []
graph = [[] for _ in range(n + 1)]
degree = [0] * (n + 1)
dq = deque()

for o in order:
    for i in range(len(o) - 1):
        graph[o[i]].append(o[i + 1])
        degree[o[i + 1]] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)

while dq:
    before = dq.popleft()
    answer.append(before)

    for after in graph[before]:
        degree[after] -= 1

        if degree[after] == 0:
            dq.append(after)


if len(answer) == n:
    for i in answer:
        print(i)
else:
    print(0)