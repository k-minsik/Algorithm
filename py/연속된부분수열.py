def solution(sequence, k):
    answer = [0, int(1e9)]
    
    l, r, t = 0, 0, sequence[0]
    sequence += [0]
    
    while r < len(sequence) - 1:
        print(l, r, t)
        if t < k:
            r += 1
            t += sequence[r]
        
        elif t == k:
            before = answer[1] - answer[0]
            now = r - l
            
            if now < before:
                answer[0] = l
                answer[1] = r

            t -= sequence[l]
            l += 1
            r += 1
            t += sequence[r]
        
        elif t > k:
            t -= sequence[l]
            l += 1
            
        
    return answer

# 	[2, 3]
# 	[6, 6]
# [2, 2, 2, 2, 2]	6
print(solution([1, 1, 1, 2, 3, 4, 5], 5))