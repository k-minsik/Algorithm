import sys
input = sys.stdin.readline

ret = 0
for _ in range(int(input())):
    q = list(input().split())

    if q[0] == "add":
        ret |= (1 << int(q[1]))
    elif q[0] == "remove":
        ret &= ~(1 << int(q[1]))
    elif q[0] == "check":
        check = ret & (1 << int(q[1]))
        if check:
            print(1)
        else:
            print(0)
    elif q[0] == "toggle":
        ret ^= (1 << int(q[1]))
    elif q[0] == "all":
        ret = (1 << 21) - 1
    elif q[0] == "empty":
        ret = 0