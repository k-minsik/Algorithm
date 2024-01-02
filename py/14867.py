import sys
from collections import deque
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
memo = {}
dq = deque([[0, 0, 0]])

answer = -1
while dq:
    nx, ny, count = dq.popleft()

    if nx == c and ny == d:
        answer = count
        break

    if (nx, ny) in memo:
        continue

    memo[(nx, ny)] = count

    # X에 물을 가득 채운다
    dq.append([a, ny, count + 1])
    dq.append([nx, b, count + 1])

    # X의 물을 모두 버린다
    dq.append([0, ny, count + 1])
    dq.append([nx, 0, count + 1])

    # X의 물을 Y에 붓는다
    if nx + ny < a:
        dq.append([nx + ny, 0, count + 1])
    else:
        dq.append([a, nx + ny - a, count + 1])
    if nx + ny < b:
        dq.append([0, nx + ny, count + 1])
    else:
        dq.append([nx + ny - b, b, count + 1])

print(answer)