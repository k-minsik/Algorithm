from sys import stdin
input = stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))

answer = []
M = int(1e9)

for i in range(n - 2):
    l = i + 1
    r = n - 1

    flag = False
    while l < r:
        ret = data[i] + data[l] + data[r]

        if abs(ret) < M:
            answer = [data[i], data[l], data[r]]
            M = abs(ret)

        if ret < 0:
            l += 1
        elif ret > 0:
            r -= 1
        else:
            flag = True
            break
    
    if flag:
        break

print(*answer)