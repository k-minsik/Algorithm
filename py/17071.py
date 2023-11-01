from collections import deque
M = 500001

n, k = map(int, input().split())
if n == k:
    print(0)
    exit()

visited = [[0, 0] for _ in range(M)]
visited[n][0] = 1
dq = deque([n])

time = 0
while dq:
    time += 1
    k += time
    if k >= M:
        print(-1)
        break

    for _ in range(len(dq)):
        x = dq.popleft()

        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx < M and not visited[nx][time % 2]:
                visited[nx][time % 2] = 1
                dq.append(nx)

    if visited[k][time % 2]:
        print(time)
        break