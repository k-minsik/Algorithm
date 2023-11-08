import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int, input().split()))
graph = [[0] * n for _ in range(n)]
for a in range(n):
    relation = list(map(int, input().split()))
    for b in relation[1:]:
        b -= 1
        graph[a][b] = 1
        graph[b][a] = 1

def check(group):
    if not group:
        return False
    
    stack = [group[0]]
    visited[stack[0]] = 1
    while stack:
        a = stack.pop()
        for b in range(n):
            if graph[a][b]:
                if b in group and not visited[b]:
                    visited[b] = 1
                    stack.append(b)

    for i in group:
        if not visited[i]:
            return False
    
    return True

def sumPeople(group):
    ret = 0
    for a in group:
        ret += people[a]
    return ret


answer = int(1e9)
for i in range(1, 1 << n):
    visited = [0] * n
    groupA = []
    groupB = []
    for j in range(n):
        if i & (1 << j):
            groupA.append(j)
        else:
            groupB.append(j)
    
    if check(groupA) and check(groupB):
        answer = min(answer, abs(sumPeople(groupA) - sumPeople(groupB)))

print(answer) if answer != int(1e9) else print(-1)