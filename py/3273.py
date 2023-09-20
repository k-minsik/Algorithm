import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

answer = 0
l, r = 0, n-1
while l < r:
    if arr[l] + arr[r] == x:
        answer +=1
        r -= 1
    elif arr[l] + arr[r] > x:
        r -= 1
    else:
        l += 1

print(answer)