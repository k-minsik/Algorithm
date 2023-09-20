import sys
input = sys.stdin.readline

tc = int(input())

for i in range(tc):
    k = int(input())
    n = int(input())

    arr = [[i for i in range(1, n+1)] for _ in range(k+1)]

    for y in range(1, k+1):
        for x in range(1, n):
            arr[y][x] = arr[y-1][x] + arr[y][x-1]

    print(arr[k][n-1])
