import sys
input = sys.stdin.readline

def check(mid):
    global n, m

    now = mid
    cnt = 1
    for i in range(n):
        if now - arr[i] < 0:
            now = mid
            cnt += 1
        
        now -= arr[i]
        
    if cnt <= m:
        return True
    else:
        return False


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

low = max(arr)
high = int(1e10)

answer = low
while low <= high:
    mid = (low + high) // 2

    if check(mid):
        answer = mid
        high = mid - 1
    else:
        low = mid + 1

print(answer)