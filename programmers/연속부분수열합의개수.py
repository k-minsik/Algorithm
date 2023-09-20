def solution(elements):
    answer = set()
    n = len(elements)
    elements = 2 * elements
    
    for i in range(n):
        for j in range(1, n + 1):
            answer.add(sum(elements[i : i + j]))
    
    return len(answer)