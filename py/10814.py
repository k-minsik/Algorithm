import sys
input = sys.stdin.readline

arr = []
n = int(input())
cnt = 1

for _ in range(n):
    a, b = input().split()
    arr.append([int(a), b, cnt])
    cnt += 1

arr.sort(key = lambda x : (x[0], x[2]))

for i in arr:
    print(i[0], i[1])
