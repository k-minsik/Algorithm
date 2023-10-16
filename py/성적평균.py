import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    start, end = map(int, sys.stdin.readline().split())
    print('{:.2f}'.format(sum(arr[start-1:end])/(end-start+1)))