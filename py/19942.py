import sys
input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
food = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9
buy = [99]


for i in range(1, 1 << n):
    sp, sf, ss, sv, sc = 0, 0, 0, 0, 0
    pick = []

    for j in range(n):
        if i & (1 << j):
            pick.append(j + 1)
            sp += food[j][0]
            sf += food[j][1]
            ss += food[j][2]
            sv += food[j][3]
            sc += food[j][4]

    if sp >= mp and sf >= mf and ss >= ms and sv >= mv:
        if sc < answer:
            answer = sc
            buy = sorted(pick)
        elif sc == answer:
            buy = sorted(min(buy, pick))

if answer != 1e9:
    print(answer)
    print(*buy)
else:
    print(-1)
