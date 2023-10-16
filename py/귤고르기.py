import heapq
def solution(k, tan):
    answer = 0
    dic = {}
    
    for i in tan:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    print(dic)
    hq = []
    for size, num in dic.items():
        heapq.heappush(hq, [-num, size])
    
    print(hq)
    while True:
        if k <= 0:
            break
            
        num, size = heapq.heappop(hq)
        k += num
        answer += 1
        print(size, num, k)
    return answer

print(solution(6, [1,3,2,5,4,5,2,3]))
print()
print(solution(4, [1,3,2,5,4,5,2,3]))
print()
print(solution(2, [1,1,1,1,2,2,2,3]))
