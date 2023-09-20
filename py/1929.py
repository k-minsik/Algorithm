a, b = map(int, input().split())

arr = [True] * (b + 1)
arr[0], arr[1] = False, False

for i in range(3, b+1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            arr[i] = False
            break

for i in range(a, b+1):
    if arr[i]:
        print(i)


