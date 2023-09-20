import sys
from collections import deque
input = sys.stdin.readline

tk = int(input())
for _ in range(tk):
    q = list(input().rstrip())
    n = int(input())
    s = input().rstrip()
    arr = deque()

    cur = ''
    if n:
        for c in s[1:]:
            if '0' <= c <= '9':
                cur += c
            elif c == ',':
                arr.append(int(cur))
                cur = ''
            elif c == ']':
                arr.append(int(cur))

    r, e = False, False
    for i in q:
        if i == "R":
            if r: r = False
            else: r = True

        elif i == "D":
            if arr:
                if r: arr.pop()
                else: arr.popleft()
            else:
                e = True
                break
    if e:
        print("error")
    else:
        if r: arr = list(arr)[::-1]
        else: arr = list(arr)
        print("[", end = "")
        if arr:
            for i in arr[:-1]:
                print(i, end =",")
            print(arr[-1], end = "")
        print("]")

        
