import sys
input = sys.stdin.readline

n, m = map(int, input().split())
point = list(map(int, input().split()))
graph = [[0] * n for _ in range(n)]
synergy = [list(map(int, input().split())) for _ in range(m)]

answer = int(-1e9)
for i in range(1 << n):
    score = 0

    for j in range(n):
        if i & (1 << j):
            score += point[j]
    
    for a, b, d in synergy:
        if (i & (1 << (a - 1))) and (i & (1 << (b - 1))):
            score += d

    answer = max(answer, score)

print(answer)