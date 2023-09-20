import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for i in range(n):
    s = input().rstrip()

    if s == "pop_front":
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif s == "pop_back":
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif s == "size":
        print(len(dq))
    elif s == "empty":
        if dq:
            print(0)
        else:
            print(1)
    elif s == "front":
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif s == "back":
        if dq:
            print(dq[-1])
        else:
            print(-1)
    else:
        ss, temp = s.split()
        if ss == "push_front":
            dq.appendleft(temp)
        else:
            dq.append(temp)
