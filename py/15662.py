import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
gear = [deque(list(input().rstrip())) for _ in range(t)]
k = int(input())
rot = [list(map(int, input().split())) for _ in range(k)]

for n, d in rot:
    n -= 1
    temp = [0 for _ in range(t)]

    temp[n] = d
    ld, rd = d, d
    # 왼쪽
    for i in range(n - 1, -1, -1):
        if gear[i][2] != gear[i + 1][6]:
            ld *= -1
            temp[i] = ld
        else:
            break
    # 오른쪽
    for i in range(n + 1, t):
        if gear[i - 1][2] != gear[i][6]:
            rd *= -1
            temp[i] = rd
        else:
            break

    for i in range(t):
        gear[i].rotate(temp[i])

answer = 0
for g in gear:
    if g[0] == '1':
        answer += 1
print(answer)