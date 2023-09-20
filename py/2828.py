n, m = map(int, input().split())
j = int(input())

b_l = 1
b_r = m

answer = 0

for k in range(j):
    w = int(input())

    if b_l <= w <= b_r:
        continue
    elif 1 <= w < b_l:
        temp = b_l - w
        b_l -= temp
        b_r -= temp
        answer += temp
    elif b_r < w <= n:
        temp = w - b_r
        b_l += temp
        b_r += temp
        answer += temp

print(answer)

