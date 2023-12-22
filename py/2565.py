import sys
input = sys.stdin.readline

line = []

n = int(input()) # n <= 100
for _ in range(n):
    a, b = map(int, input().split()) # a, b <= 500
    line.append([a, b])

line.sort()

print(line)