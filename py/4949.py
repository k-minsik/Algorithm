arr = ['(', ')', '[', ']']

while True:
    s = input().rstrip()
    if s == ".": break
    s = list(s)

    st = []
    while s:
        temp = s.pop()
        if temp in arr:
            if st:
                if (st[-1] == ")" and temp == "(") or (st[-1] == "]" and temp == "["):
                    st.pop()
                else:
                    if temp == "(" or temp == "[":
                        st.append(temp)
                        break
                    else:
                        st.append(temp)
            else:
                if temp == "(" or temp == "[":
                        st.append(temp)
                        break
                else:
                    st.append(temp)
    
    if st: print("no")
    else: print("yes")