import sys
input = sys.stdin.readline

st = []
for _ in range(int(input())):
    s = input().rstrip()

    if s == "pop":
        if st:
            print(st.pop())
        else:
            print(-1)
    elif s == "size":
        print(len(st))
    elif s == "empty":
        if st:
            print(0)
        else:
            print(1)
    elif s == "top":
        if st:
            print(st[-1])
        else:
            print(-1)
    else:
        _, num = s.split()
        st.append(int(num))