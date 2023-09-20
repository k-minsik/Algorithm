def dfs():
    if len(answer) == m:
        for i in answer:
            print(i, end = " ")
        print()
        return 
    
    for i in range(1, n + 1):
        if not visited[i]:
            answer.append(i)
            visited[i] = 1
            dfs()
            answer.pop()
            visited[i] = 0

n, m = map(int, input().split())
visited = [0 for _ in range(n + 1)]
answer = []
dfs()