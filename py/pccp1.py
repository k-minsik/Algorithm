def solution(bandage, health, attacks):
    answer = health
    t, x, y = bandage
    
    prev = 0
    for time, damage in attacks:
        answer += (time - prev - 1) * x + ((time - prev - 1) // t) * y
        answer = min(health, answer)
        answer -= damage
        
        if answer <= 0:
            return -1
        
        prev = time

    return answer if answer > 0 else -1