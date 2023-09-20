import sys
input = sys.stdin.readline

n = int(input())
t = [[] for _ in range(n)]
temp = list(map(int, input().split()))
e = int(input())


for i in range(n):
    if temp[i] == -1:
        root = i
    else:
        t[temp[i]].append(i)

answer = 0 
st = [root]
if e == root: print(0)
else:
    while st:
        cur = st.pop()
        if len(t[cur]) != 0:
            if len(t[cur]) == 1 and t[cur][0] == e:
                print(t[cur])
                answer += 1
            else:
                for c in t[cur]:
                    if c != e:
                        st.append(c)
        else:
            answer += 1

    print(answer)

print(t)

        