answer = 0
for tk in range(1, int(input())+1):
    answer = 0
    n = int(input())
    nq = [0] * n

    def check(cur):
        for i in range(cur):
            if nq[cur] == nq[i] or cur - i == abs(nq[cur] - nq[i]):
                return False
        return True

    def dfs(cur):
        global answer

        if cur == n:
            answer += 1
        
        else:
            for i in range(n):
                nq[cur] = i
                if check(cur):
                    dfs(cur+1)
                    
    dfs(0)

    print('#{} {}'.format(tk, answer))