def solution(sequence, k):
    answer = [0, int(1e9)]
    
    l, r = 0, 0
    t = sequence[0]

    while r < len(sequence):
        if t < k and r < len(sequence) - 1:
            r += 1
            t += sequence[r]
        elif t >= k:
            if t == k:
                if r - l < answer[1] - answer[0]:
                    answer = [l, r]
            t -= sequence[l]
            l += 1
        else:
            break

    return answer