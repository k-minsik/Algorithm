arr = [True] * 250000
arr[0], arr[1] = False, False

for i in range(3, 250000):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            arr[i] = False
            break

while 1:
    n = int(input())
    if n == 0:
        break

    print(arr[n+1:2*n+1].count(True))



