import sys
input = sys.stdin.readline

n, m = map(int, input().split())
vehicle = list(map(int, input().split()))

if n <= m:
    print(n)
    exit()

answer = n
lo, hi = 0, int(1e12)
while lo <= hi:
    mid = (lo + hi) // 2

    temp = m
    for v in vehicle:
        temp += mid // v

    if n <= temp:
        answer = mid
        hi = mid - 1

    else:
        lo = mid + 1

temp = m
for v in vehicle:
    temp += (answer - 1) // v

for i in range(m):
    if answer % vehicle[i] == 0:
        temp += 1
    
    if temp == n:
        print(i + 1)
        exit()