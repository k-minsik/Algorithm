import sys
input = sys.stdin.readline

n, k = map(int, input().split())
turn = list(map(int, input().split()))

answer = 0
using = []

for i in range(k):
    if turn[i] in using:
        continue

    if len(using) < n:
        using.append(turn[i])
        continue

    select, useLast = -1, -1
    for j in using:
        if j not in turn[i:]:
            select = j
            break

        useWhen = turn[i:].index(j)
        if useLast < useWhen:
            useLast = useWhen
            select = j

    using[using.index(select)] = turn[i]
    answer += 1

print(answer)