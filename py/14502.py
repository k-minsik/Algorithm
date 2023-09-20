from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())
lab = []
zero = []
virus = deque()

for i in range(n):
    v = list(map(int, input().split()))
    lab.append(v)
    for j in range(len(v)):
        if v[j] == 2:
            virus.append([i, j])
        elif v[j] == 0:
            zero.append([i, j])

res = 0
for z in combinations(zero, 3):
    lab_tmp = copy.deepcopy(lab)
    virus_tmp = copy.deepcopy(virus)
    lab_tmp[z[0][0]][z[0][1]] = 1
    lab_tmp[z[1][0]][z[1][1]] = 1
    lab_tmp[z[2][0]][z[2][1]] = 1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while virus_tmp:
        x, y = virus_tmp.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if lab_tmp[nx][ny] == 0:
                    lab_tmp[nx][ny] = 2
                    virus_tmp.append([nx, ny])

    cnt = 0
    for l in lab_tmp:
        cnt += l.count(0)
    
    if cnt > res:
        res = cnt


print(res)

