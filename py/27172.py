import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
score = [0] * 1000001
visited = [False] * 1000001

M = 0
for i in card:
    visited[i] = True
    M = max(M, i)

for i in card:
    j = 2
    while True:
        if i * j > M:
            break
        
        if visited[i * j]:
            score[i] += 1
            score[i * j] -= 1

        j += 1

for i in card:
    print(score[i], end = " ")