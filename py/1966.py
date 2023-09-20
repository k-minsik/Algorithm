import sys
from collections import deque
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    n, m = map(int, input().split())

    arr = deque([i for i in range(n)])
    order = deque(list(map(int, input().split())))
    cnt = 0

    while 1:
        if order[0] == max(order):
            cnt += 1
            if arr[0] == m:
                print(cnt)
                break
            else:
                arr.popleft()
                order.popleft()
        else:
            arr.append(arr.popleft())
            order.append(order.popleft())