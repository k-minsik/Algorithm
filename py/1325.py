import sys
input = sys.stdin.readline

def dfs(i):
    cnt = 1
    visited[i] = 1
    st = [i]

    while st:
        cur = st.pop()
        for c in arr[cur]:
            if visited[c] == 0:
                cnt += 1
                st.append(c)

    return cnt


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
mx = -1

for _ in range(m):
    a, b = map(int, input().split())
    arr[b].append(a)

answer = []
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    temp = dfs(i)
    if temp > mx:
        answer = []
        answer.append(i)
        mx = temp
    elif temp == mx:
        answer.append(i)
    else:
        continue
    
      
for i in answer:
    print(i, end = " ")
