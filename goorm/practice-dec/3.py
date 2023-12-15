import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

a, b = list(input().split()), list(input().split())
A, B = defaultdict(int), defaultdict(int)

for i in range(n):
    A[a[i]] = 1
    B[b[i]] = 1

for i in range(m):
    a, b = map(str, input().split())

    if a in A and b in B:
        A[b] = 1
        B[a] = 1
        A.pop(a)
        B.pop(b)

answer = []
for k in A.keys():
    answer.append(k)

print(*sorted(answer))