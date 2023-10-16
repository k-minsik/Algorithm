def dfs(idx, now, kcal):
    if idx == n:
        score.append(now)
        return

    if kcal + arr[idx][1] <= l:
        dfs(idx+1, now+arr[idx][0], kcal+arr[idx][1])
    dfs(idx+1, now, kcal)


for tk in range(1, int(input())+1):
    answer = 0
    n, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    score = []

    dfs(0, 0, 0)


    print('#{} {}'.format(tk, max(score)))