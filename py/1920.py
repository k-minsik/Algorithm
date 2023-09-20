import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
data = {}
for i in arr:
    data[i] = 1

m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in data:
        print(1)
    else:
        print(0)