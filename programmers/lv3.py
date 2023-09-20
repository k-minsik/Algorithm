def solution1(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    def dfs(c):
        st = [c]
        while st:
            print(st)
            c = st.pop()
            for i in range(n):
                if c != i and computers[c][i] == 1:
                    if visited[i] == 0:
                        visited[i] = 1
                        st.append(i)

    for c in range(n):
        if visited[c] == 0:
            visited[c] = 1
            dfs(c)
            answer += 1
            
    return answer

def solution2(m, n, puddles):
    arr = [[0 for _ in range(m+1)] for _ in range(n)]
    arr[1][1] = 1
    
    for p in puddles:
        arr[p[1]][p[0]] = -1
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == -1: 
                arr[i][j] = 0
                continue
            else:
                arr[i][j] += arr[i-1][j] + arr[i][j-1]

    return arr[n][m] % 1000000007

from collections import deque
def solution4(program):
    answer = []
    while(program):
        program = deque(sorted(program, key= lambda x : (x[1], x[0])))
        temp = program.popleft()
        end = temp[2]
        



    return answer

solution4([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]])
solution4([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]])

