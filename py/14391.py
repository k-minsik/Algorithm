n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

answer = 0
for i in range(1 << (n * m)):
    temp = 0
    for y in range(n):
        cur = 0
        for x in range(m):
            if (i & (1 << (y * m) + x)) == 0:
                cur = cur * 10 + int(arr[y][x])
            else:
                temp += cur
                cur = 0
    
        temp += cur

    for x in range(m):
        cur = 0
        for y in range(n):
            if (i & (1 << (y * m) + x)) != 0:
                cur = cur * 10 + int(arr[y][x])
            else:
                temp += cur
                cur = 0
    
        temp += cur
    
    answer = max(answer, temp)

print(answer)