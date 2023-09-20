import sys
from itertools import permutations
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rot = [list(map(int, input().split())) for _ in range(k)]
answer = int(1e9)

def rotate(arr, y, x, d):
    dq = deque()
    for i in range(x, x + d):
        dq.append(arr[y][i])
    for i in range(y + 1, y + d):
        dq.append(arr[i][x + d - 1])
    for i in range(x + d - 2, x - 1, -1):
        dq.append(arr[y + d - 1][i])
    for i in range(y + d - 2, y, -1):
        dq.append(arr[i][x])

    dq.rotate(1)

    for i in range(x, x + d):
        arr[y][i] = dq.popleft()
    for i in range(y + 1, y + d):
        arr[i][x + d - 1] = dq.popleft()
    for i in range(x + d - 2, x - 1, -1):
        arr[y + d - 1][i] = dq.popleft()
    for i in range(y + d - 2, y, -1):
        arr[i][x] = dq.popleft()

    return arr

for p in permutations(rot, k):
    temp = deepcopy(arr)
    for r, c, s in p:
        y = r - s - 1
        x = c - s - 1
        d = 2 * s + 1

        while d > 0:
            temp = rotate(temp, y, x, d)
            y += 1
            x += 1
            d -= 2
            
    for i in temp:
        answer = min(answer, sum(i))

print(answer)