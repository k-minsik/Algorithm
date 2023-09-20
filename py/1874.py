import sys
input = sys.stdin.readline

n = int(input())

can = True
st = [1]
now = 1
answer = ['+']

for i in range(n):
    temp = int(input())

    while 1:
        if now > n:
            can = False
            break
        if  st and st[-1] == temp:
            st.pop()
            answer.append('-')
            break

        now += 1
        st.append(now)
        answer.append('+')

if can:
    for i in answer:
        print(i)
else:
    print("NO")

