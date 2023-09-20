import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
temp = n

while temp > cnt:
    temp -= cnt
    cnt += 1

print(str(temp) + "/" + str(cnt + 1 - temp) if cnt % 2 == 0 else str(cnt + 1 - temp) + "/" + str(temp))
