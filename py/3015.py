import sys
input = sys.stdin.readline

n = int(input())
st = []
answer = 0

for _ in range(n):
    now = int(input())
    cnt = 1

    while st and st[-1][0] <= now:
        answer += st[-1][1]
        if now == st[-1][0]:
            cnt = st[-1][1] + 1
        else:
            cnt = 1
        
        st.pop()
    if st:
        answer += 1
    st.append([now, cnt])

print(answer)
