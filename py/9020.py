arr = [True] * 10001
arr[0], arr[1] = False, False

for i in range(3, 10001):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            arr[i] = False
            break

for i in range(int(input())):
    n = int(input())
    a, b = n // 2, n // 2

    while a > 1:
        if arr[a] and arr[b]:
            print(a, b)
            break
        a -= 1
        b += 1

