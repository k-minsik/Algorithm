import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    st = []
    arr = list(input().rstrip())

    while arr:
        temp = arr.pop()
        
        if st:
            if st[-1] != temp:
                st.pop()
            else:
                st.append(temp)
        else:
            if temp == '(':
                st.append(temp)
                break
            else:
                st.append(temp)

    if st: print("NO")
    else: print("YES")
