r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in 
range(r)]

for i in range(r):
    temp = list(map(int, input().split()))
    for j in range(c):
        a[i][j] += temp[j]

for i in range(r):
    for j in range(c):
        print(a[i][j], end = ' ')
    print()