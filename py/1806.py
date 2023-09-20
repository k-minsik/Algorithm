import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
l, r = 0, 0

temp = arr[0]
answer = int(1e9)
while True:
    if l > r:
        break

    if temp >= s:
        answer = min(answer, r - l + 1)

        temp -= arr[l]
        l += 1
        
    else:
        r += 1
        if r == n:
            break
        temp += arr[r]    

print(0 if answer == int(1e9) else answer)