import sys
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cctv = [[0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3]]


answer = n * m
for a in cctv[0]:
    for b in cctv[1]:
        for c in cctv[2]:
            for d in cctv[3]:

                arr = deepcopy(graph)
                for y in range(n):
                    for x in range(m):

                        if arr[y][x] == 1:
                            if a == 0:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                            elif a == 1:
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                            elif a == 2:
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif a == 3:
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break

                        elif arr[y][x] == 2:
                            if b == 0:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif b == 1:
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break

                        elif arr[y][x] == 3:
                            if c == 0:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                            elif c == 1:
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif c == 2:
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break
                            
                            elif c == 3:
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break


                        elif arr[y][x] == 4:
                            if d == 0:
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif d == 1:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif d == 2:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break
                                for t in range(y + 1, n):
                                    if arr[t][x] != 6:
                                        arr[t][x] = "#"
                                    else:
                                        break
                            elif d == 3:
                                for t in range(1, y + 1):
                                    if arr[y - t][x] != 6:
                                        arr[y - t][x] = "#"
                                    else:
                                        break
                                for t in range(1, x + 1):
                                    if arr[y][x - t] != 6:
                                        arr[y][x - t] = "#"
                                    else:
                                        break
                                for t in range(x + 1, m):
                                    if arr[y][t] != 6:
                                        arr[y][t] = "#"
                                    else:
                                        break

                        elif arr[y][x] == 5:
                            for t in range(1, y + 1):
                                if arr[y - t][x] != 6:
                                    arr[y - t][x] = "#"
                                else:
                                    break
                            for t in range(1, x + 1):
                                if arr[y][x - t] != 6:
                                    arr[y][x - t] = "#"
                                else:
                                    break
                            for t in range(x + 1, m):
                                if arr[y][t] != 6:
                                    arr[y][t] = "#"
                                else:
                                    break
                            for t in range(y + 1, n):
                                if arr[t][x] != 6:
                                    arr[t][x] = "#"
                                else:
                                    break

                temp = n * m 
                for i in range(n):
                    for j in range(m):
                        if arr[i][j] in ["#", 1, 2, 3, 4, 5, 6]:
                            temp -= 1

                answer = min(answer, temp)

print(answer)