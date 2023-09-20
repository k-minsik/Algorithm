x, y = map(int, input().split())
z = y * 100 // x

if z >= 99:
    print(-1)
else:
    answer = 0
    lo = 1
    hi = x
    while lo <= hi:
        mid = (lo + hi) // 2
        temp = (y + mid) * 100 // (x + mid)

        if temp > z:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1

    print(answer)