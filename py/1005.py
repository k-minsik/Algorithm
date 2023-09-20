import sys
from collections import deque
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    degree = [0 for _ in range(n + 1)]
    build = [[] for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]
    
    for _ in range(k):
        now, next = map(int, input().split())
        build[now].append(next)
        degree[next] += 1

    dq = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)
            dp[i] = time[i]

    while dq:
        now = dq.popleft()

        for next in build[now]:
            degree[next] -= 1
            dp[next] = max(dp[next], dp[now] + time[next])

            if degree[next] == 0:
                dq.append(next)
    
    print(dp[int(input())])