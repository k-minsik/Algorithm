a = list(map(int, input().split()))
a.sort()
while 1:
    if a[-1] < a[0] + a[1]:
        answer = sum(a)
        break
    a[-1] -= 1

print(answer)
