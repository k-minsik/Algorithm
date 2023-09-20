from copy import deepcopy
n = int(input())

t = []
p = []
visited = [True for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    if i + a > n:
        visited[i] = False

answer = 0
for i in range(1 << n):
    visited2 = deepcopy(visited)
    temp = 0
    for j in range(n):
        if i & (1 << j) and visited2[j]:
            temp += p[j]
            for k in range(t[j]):
                visited2[j + k] = False
    
    answer = max(answer, temp)

print(answer)