import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
homes = []
stores = []

for y in range(n):
    row = list(map(int, input().split()))
    for x in range(n):
        if row[x] == 1:
            homes.append([y, x])
        elif row[x] == 2:
            stores.append([y, x])

answer = 1e9
for store in combinations(stores, m):
    distSum = 0
    for home in homes:
        distance = 1e9
        for s in store:
            distance = min(distance, abs(home[0] - s[0]) + abs(home[1] - s[1]))
        distSum += distance
    answer = min(answer, distSum)

print(answer)