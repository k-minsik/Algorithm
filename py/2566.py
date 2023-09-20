import sys
input = sys.stdin.readline
y, x = -1, -1
MAX = -1
for i in range(1, 10):
    temp = list(map(int, input().split()))
    m = max(temp)

    if m > MAX:
        MAX = m
        y = i
        x = temp.index(m) + 1

print(MAX)
print(y, x)
    