def possible(cur, graph):
    for i in range(cur):
        if graph[i] == graph[cur] or abs(i - cur) == abs(graph[i] - graph[cur]):
            return False
    
    return True
        
def nqueen(n, cur, graph):
    result = 0
    if cur == n:
        return 1

    for i in range(n):
        graph[cur] = i

        if possible(cur, graph):
            result += nqueen(n, cur+1, graph)

    return result

def solution(n):
    arr = [0] * n
    return nqueen(n, 0, arr)
