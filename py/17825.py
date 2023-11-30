import sys
input = sys.stdin.readline

def dfs(round, tempAnswer):
    global answer

    if round == 10:
        answer = max(answer, tempAnswer)
        return
    
    for i in range(4):
        x, initX = horse[i], horse[i]
        if x == 21:
            continue

        move = dice[round]
        if x in [5, 10, 15]:
            x = graph[x][1]
            move -= 1
        
        for _ in range(move):
            x = graph[x][0]

        if x == 21 or (x not in horse):
            horse[i] = x
            dfs(round + 1, tempAnswer + score[x])
            horse[i] = initX
        
graph = [[1],[2],[3],[4],[5],[6,22],[7],[8],[9],[10],[11,29],[12],[13],[14],[15],[16,28],[17],[18],[19],[20],[21],[21],
         [23],[24],[25],[31],[25],[26],[27],[30],[25],[32],[20]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0,
         13, 16, 19, 25, 26, 27, 28, 22, 24, 30, 35]

dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]
answer = 0
dfs(0, 0)
print(answer)