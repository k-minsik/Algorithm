arr = [[0 for _ in range(100)] for _ in range(100)]
for i in range(int(input())):
    a, b = map(int, input().split())
    for y in range(a, a+10):
        for x in range(b, b+10):
            arr[y][x] = 1

ret = 0
for i in range(100):
    ret += arr[i].count(1)

print(ret)


