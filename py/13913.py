from collections import deque
n, k = map(int, input().split())
arr = [0] * 222222
visited = [0] * 222222
record = []

visited[n] = 1

dq = deque()
dq.append(n)

dx = [[1, 1], [1, -1], [2, 0]]

while dq:
    now = dq.popleft()

    if now == k:
        answer = visited[now]
        break

    for i in range(3):
        next = now * dx[i][0] + dx[i][1]
        if 0 <= next <= 200001:
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                dq.append(next)
                arr[next] = now

now = k
record.append(k)

while now != n:
    now = arr[now]
    record.append(now)

print(visited[k] - 1)
for i in record[::-1]:
    print(i, end = " ")