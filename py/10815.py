import sys
input = sys.stdin.readline

n = int(input())
have = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

d = {}
for i in have:
    d[i] = 1

for i in check:
    if i in d:
        print(1, end = " ")
    else:
        print(0, end = " ")