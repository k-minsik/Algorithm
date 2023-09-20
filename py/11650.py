import sys
input = sys.stdin.readline

# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort()

for i in arr:
    print(i[0], end = " ")
    print(i[1])
