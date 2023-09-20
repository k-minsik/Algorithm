import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

l, x, r, y = 0, 0, n - 1, n - 1
ret = abs(arr[r] + arr[l])

while True:
    if l == r:
        break

    temp = arr[r] + arr[l]
    if abs(temp) < ret:
        ret = abs(temp)
        x = l
        y = r
        
        if temp == 0:
            break

    if temp < 0:
        l += 1
    else:
        r -= 1 

print(arr[x], arr[y])