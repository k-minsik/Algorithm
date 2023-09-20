import sys
input = sys.stdin.readline

n = int(input())
point = []

for _ in range(n):
    x, y = map(int, input().split())
    point.append([x, y])
point.append(point[0])

xtemp, ytemp = 0, 0
for i in range(n):
    x1, y1 = point[i]
    x2, y2 = point[i + 1] 
    xtemp += x1 * y2
    ytemp += y1 * x2

print(round(abs(xtemp - ytemp) / 2, 1))
    