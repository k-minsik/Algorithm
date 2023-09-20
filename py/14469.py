n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

t = arr[0][0] + arr[0][1]
for i in range(1, n):
    t = max(t, arr[1][0])
    t += arr[1][1]

print(t)
