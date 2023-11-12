# import sys
# input = sys.stdin.readline

# ret = 0
# for _ in range(int(input())):
#     q = list(input().split())

#     if q[0] == "add":
#         ret |= (1 << int(q[1]))
#     elif q[0] == "remove":
#         ret &= ~(1 << int(q[1]))
#     elif q[0] == "check":
#         check = ret & (1 << int(q[1]))
#         if check:
#             print(1)
#         else:
#             print(0)
#     elif q[0] == "toggle":
#         ret ^= (1 << int(q[1]))
#     elif q[0] == "all":
#         ret = (1 << 21) - 1
#     elif q[0] == "empty":
#         ret = 0


import sys
input = sys.stdin.readline

answer = 0

m = int(input())
for _ in range(m):
    row = list(input().split()) + [0]
    cmd, num = row[0], row[1]
    num = 1 << int(num)

    if cmd == "add":
        answer |= num
        
    elif cmd == "remove":
        answer &= ~num

    elif cmd == "check":
        if answer & num:
            print(1)
        else:
            print(0)

    elif cmd == "toggle":
        answer ^= num

    elif cmd == "all":
        answer = (1 << 21) - 1

    elif cmd == "empty":
        answer = 0