import sys
from collections import deque
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    a, b = map(int, input().split())
    visited = [False] * 10000

    dq = deque()
    dq.append([a, ""])
    while dq:
        now, order = dq.popleft()

        if now == b:
            print(order)
            break

        next = (now * 2) % 10000
        if not visited[next]:
            visited[next] = True
            dq.append([next, order + "D"])
        
        next = (now - 1) % 10000
        if not visited[next]:
            visited[next] = True
            dq.append([next, order + "S"])
        
        next = (now * 10) % 10000 + now // 1000
        if not visited[next]:
            visited[next] = True
            dq.append([next, order + "L"])
        
        next = (now % 10) * 1000 + now // 10
        if not visited[next]:
            visited[next] = True
            dq.append([next, order + "R"])