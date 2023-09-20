a, b = map(int, input().split())
c = int(input())
n = int(input())

c -= a
flag = 0
for i in range(n, 101):
    if c * i - b < 0:
        flag = 1

print(0 if flag else 1)
    