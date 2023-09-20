import sys
input = sys.stdin.readline

a, b = 0, 0
cnt_a, cnt_b = 0, 0

def func(team, now):
    team += now - prev
    return team


n = int(input())

prev = 0
for _ in range(n):
    g, t = input().split()
    t = int(t[:2]) * 60 + int(t[3:])

    if a > b: cnt_a = func(cnt_a, t)
    elif b > a: cnt_b = func(cnt_b, t)

    if g == "1": a += 1
    elif g == "2": b += 1

    prev = t

if a > b: cnt_a = func(cnt_a, 48*60)
elif b > a: cnt_b = func(cnt_b, 48*60)

print(str(cnt_a//60).zfill(2) + ":" + str(cnt_a%60).zfill(2))
print(str(cnt_b//60).zfill(2) + ":" + str(cnt_b%60).zfill(2))
