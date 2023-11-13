import sys
input = sys.stdin.readline

n = int(input())
cows = [list(map(int, input().split())) for _ in range(n)]

time = 0
for enter, take in sorted(cows):
    if enter <= time:
        time += take
    else:
        time = enter + take

print(time)