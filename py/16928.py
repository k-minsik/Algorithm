import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0 for _ in range(101)]
arr[1] = 1

sa, bam = {}, {}
for i in range(n):
    a, b = map(int, input().split())
    sa[a] = b
for j in range(m):
    a, b = map(int, input().split())
    bam[a] = b

dq = deque()
dq.append(1)
while dq:
    cur = dq.popleft()

    if cur == 100:
        break

    for d in range(1, 7):
        nx = cur + d

        if 0 <= nx <= 100:
            if nx in sa:
                nx = sa[nx]
            elif nx in bam:
                nx = bam[nx]
            if not arr[nx]:
                dq.append(nx)
                arr[nx] = arr[cur] + 1
print(arr[100])
