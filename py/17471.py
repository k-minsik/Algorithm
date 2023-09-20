import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
man = [0] + list(map(int, input().split()))
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    
    for j in range(1, temp[0]+1):
        arr[i][temp[j]] = 1

for i in range(1, n):
    for comb in combinations(range(1, n+1), )