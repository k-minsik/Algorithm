import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
reverseGraph = deepcopy(graph)
answer = 1e9

for y in range(n):
    for x in range(n):
        if reverseGraph[y][x] == 'H':
            reverseGraph[y][x] = 'T'
        else:
            reverseGraph[y][x] = 'H'

# for i in graph:
#     print(i)
# print(12312354124)
# for i in reverseGraph:
#     print(i)

for i in range(1 << n):
    tempGraph = []
    for j in range(n):
        if i & (1 << j):
            tempGraph.append(reverseGraph[j])
        else:
            tempGraph.append(graph[j])
            
    ret = 0
    for y in range(n):
        cnt = 0
        for x in range(n):
            if tempGraph[x][y] == 'T':
                cnt += 1
        ret += min(cnt, n - cnt)
    
    answer = min(answer, ret)

print(answer)