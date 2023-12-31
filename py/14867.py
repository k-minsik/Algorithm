import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b, c, d):
    m = {}
    dq = deque()

    def enqueue(x, y, depth):
        if (x, y) in m:
            return
        m[(x, y)] = depth + 1
        dq.append((x, y))

    m[(0, 0)] = 1
    dq.append((0, 0))

    while dq:
        x, y = dq.popleft()

        enqueue(a, y, m[(x, y)])
        enqueue(x, b, m[(x, y)])
        enqueue(0, y, m[(x, y)])
        enqueue(x, 0, m[(x, y)])
        enqueue(min(x + y, a), max(0, x + y - a), m[(x, y)])
        enqueue(max(0, x + y - b), min(x + y, b), m[(x, y)])

    return m.get((c, d), -1) - 1

a, b, c, d = map(int, input().split())
answer = bfs(a, b, c, d)
print(answer if answer >= 0 else -1)