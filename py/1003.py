import sys
input = sys.stdin.readline

ret = [[1, 0], [0, 1]]
for i in range(2, 41):
    ret.append([ret[i-1][0] + ret[i-2][0], ret[i-1][1] + ret[i-2][1]])

tk = int(input())
for _ in range(tk):
    n = int(input())
    print(ret[n][0], ret[n][1])
