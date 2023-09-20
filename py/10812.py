n, m = map(int, input().split())

arr = [i for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a:b+1] = arr[c:b+1] + arr[a:c]

for i in range(1, n+1):
    print(arr[i] , end = " ")