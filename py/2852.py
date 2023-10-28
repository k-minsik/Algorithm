# import sys
# input = sys.stdin.readline

# a, b = 0, 0
# cnt_a, cnt_b = 0, 0

# def func(team, now):
#     team += now - prev
#     return team


# n = int(input())

# prev = 0
# for _ in range(n):
#     g, t = input().split()
#     t = int(t[:2]) * 60 + int(t[3:])

#     if a > b: cnt_a = func(cnt_a, t)
#     elif b > a: cnt_b = func(cnt_b, t)

#     if g == "1": a += 1
#     elif g == "2": b += 1

#     prev = t

# if a > b: cnt_a = func(cnt_a, 48*60)
# elif b > a: cnt_b = func(cnt_b, 48*60)

# print(str(cnt_a//60).zfill(2) + ":" + str(cnt_a%60).zfill(2))
# print(str(cnt_b//60).zfill(2) + ":" + str(cnt_b%60).zfill(2))


import sys
input = sys.stdin.readline

score = 0
gameOver = 48 * 60
n = int(input())

A, B = 0, 0
win = ''
for _ in range(n):
    who, when = map(str, input().split())

    event = int(when[:2]) * 60 + int(when[3:])

    if score > 0:
        A += event - prevEvent
    
    elif score < 0:
        B += event - prevEvent

    score += 1 if who == '1' else -1
    prevEvent = event

if score > 0:
    A += gameOver - event
elif score < 0:
    B += gameOver - event

print(str(A // 60).zfill(2) + ":" + str(A % 60).zfill(2))
print(str(B // 60).zfill(2) + ":" + str(B % 60).zfill(2))