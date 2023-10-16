from collections import deque
def solution(priorities, location):
    answer = 0
    p = deque() # [location, priority]

    for i in range(len(priorities)):
        p.append([i, priorities[i]])

    while p:
        loc, pri = p.popleft()

        if pri >= max([i[1] for i in p]):
            answer += 1
            if loc == location:
                return answer
        else:
            p.append([loc, pri])
        


print(solution([2,1,3,2], 2)) # 1
print(solution([1,1,9,1,1,1], 0)) # 5