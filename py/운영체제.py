from heapq import heappop, heappush, heapify
from collections import deque

def call(p, w, now):
    while p and p[0][1] <= now:
        heappush(w, p.popleft())
    return p, w

def solution4(program):
    answer = [0 for _ in range(11)]
    program.sort(key= lambda x: (x[1], x[0]))
    p = deque(program)
    w = []
    
    now = 0
    while p or w:
        if not w:
            now = p[0][1]
        else:
            a, b, c = heappop(w)
            answer[a] += now - b
            now += c
        
        p, w = call(p, w, now)
        
    answer[0] = now
    return answer