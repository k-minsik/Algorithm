import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

d = {}
for i in have:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in check:
    if i in d:
        print(d[i], end = " ")
    else:
        print(0, end = " ")