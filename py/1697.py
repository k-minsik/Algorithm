from collections import deque

n, k = map(int, input().split())
dq = deque()
arr = [0 for _ in range(100001)]
dq.append(n)

while dq:
    cur = dq.popleft()

    if cur == k:
        break

    for nx in (cur+1, cur-1, cur*2):
        if 0 <= nx <= 100000 and arr[nx] == 0:
            arr[nx] = arr[cur] + 1
            dq.append(nx)

print(arr[k])