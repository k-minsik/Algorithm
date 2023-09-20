n, b = map(int, input().split())

cnt = 0
while b ** cnt <= n:
    cnt += 1

answer = ""
for i in range(1, cnt + 1):
    up = cnt - i
    temp = n // (b ** up)
    n %= (b ** up)
    if temp > 9:
        answer += chr(temp + 55)
    else:
        answer += str(temp)

print(answer)