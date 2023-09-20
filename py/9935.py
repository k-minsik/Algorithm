s = input()
b = input()
st = []
l = len(b)

for i in range(len(s)):
    st.append(s[i])

    if ''.join(st[-l:]) == b:
        for _ in range(l):
            st.pop()


if st:
    print(''.join(st))
else:
    print("FRULA")