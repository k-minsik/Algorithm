graph = [[i + 1] for i in range(21)] + [[] for _ in range(12)]
graph[5].append(22), graph[10].append(25), graph[15].append(27)
graph[22].append(23), graph[23].append(24), graph[24].append(30)
graph[25].append(26), graph[26].append(30)
graph[27].append(28), graph[28].append(29), graph[29].append(30)
graph[30].append(31), graph[31].append(32), graph[32].append(20)

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 
         30, 32, 34, 36, 38, 40, 0, 13, 16, 19, 22, 24, 29, 27,
         26, 25, 30, 35]
visited = [0 for _ in range(33)]

dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]
answer = 0

def go(cnt, temp):
    global answer
    if cnt == 10:
        answer = max(answer, temp)
        return
    
    for i in range(4):
        if horse[i] == 21:
            continue
        now = horse[i]

        move = dice[cnt]
        if len(graph[horse[i]]) == 2:
            horse[i] = graph[horse[i]][1]
            move -= 1

        while move > 0:
            if horse[i] == 21:
                break
            horse[i] = graph[horse[i]][0]
            move -= 1
        
        if horse[i] != 21 and visited[horse[i]] == 1:
            visited[now] = 1
            horse[i] = now
            continue
        else:
            visited[now] = 0
            visited[horse[i]] = 1
            go(cnt + 1, temp + score[horse[i]])
            visited[horse[i]] = 0
            horse[i] = now
            visited[now] = 1

go(0, 0)
print(answer)
