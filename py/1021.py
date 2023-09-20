import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])

cnt = 0
for i in arr:
    if i == dq[0]:
        dq.popleft()
    else:
        if dq.index(i) < len(dq) - dq.index(i):
            while dq[0] != i:
                dq.append(dq.popleft())
                cnt += 1
            dq.popleft()
        else: 
            while dq[0] != i:
                dq.appendleft(dq.pop())
                cnt += 1
            dq.popleft()
print(cnt)