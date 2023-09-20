import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sarr = sorted(set(arr))
d = {}
for i in range(len(sarr)):
    d[sarr[i]] = i
for i in arr:
    print(d[i], end = " ")