from collections import deque

n, k = map(int, input().split())
arr = [-1] * 100001
arr[n] = 0
dq = deque()
dq.append(n)

while dq:
    x = dq.popleft()

    if x == k:
        print(arr[k])
        break

    if 0 <= x - 1 < 100001 and arr[x - 1] == -1:
        arr[x - 1] = arr[x] + 1
        dq.append(x - 1)

    if 0 <= 2 * x < 100001 and arr[2 * x] == -1:
        arr[2 * x] = arr[x]
        dq.append(2 * x)
    
    if 0 <= x + 1 < 100001 and arr[x + 1] == -1:
        arr[x + 1] = arr[x] + 1
        dq.append(x + 1)