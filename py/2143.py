import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
brr = list(map(int, input().split()))

dic = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        dic[sum(arr[i:j + 1])] += 1

answer = 0
for i in range(m):
    for j in range(i, m):
        answer += dic[t - sum(brr[i:j + 1])]

print(answer)