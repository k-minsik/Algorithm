import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
foods = [[5 for _ in range(n)] for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(m):
    y, x, age = map(int, input().split())
    y -= 1
    x -= 1
    tree[y][x].append(age)

for _ in range(k):
    #봄여름
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp = []
                food = 0
                for t in tree[i][j]:
                    if foods[i][j] >= t:
                        foods[i][j] -= t
                        temp.append(t + 1)
                    else:
                        food += t // 2
                tree[i][j] = temp
                foods[i][j] += food

    #가을
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for t in tree[i][j]:
                    if t % 5 == 0:
                        for d in range(8):
                            ny = i + dy[d]
                            nx = j + dx[d]

                            if 0 <= ny < n and 0 <= nx < n:
                                tree[ny][nx].append(1)

    #겨울
    for i in range(n):
        for j in range(n):
            foods[i][j] += arr[i][j]

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(tree[i][j])

print(answer)
