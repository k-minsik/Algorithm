import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = [0] * (n + 1)

for _ in range(m):
    basketNum, command, ballCount = map(int, input().split())

    if command == 1:
        basket[basketNum] += ballCount

    elif command == 2:
        if basket[basketNum] >= ballCount:
            basket[basketNum] -= ballCount

for i in range(1, n + 1):
    print(basket[i])