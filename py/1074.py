n, r, c = map(int, input().split())
answer = 0

while True:
    if n == 0:
        break
    
    n -= 1
    temp = 2 ** n
    if r < temp and c < temp:
        continue
    elif r < temp and c >= temp:   
        c -= temp
        answer += (temp ** 2)
        continue
    elif r >= temp and c < temp:
        r -= temp
        answer += (temp ** 2) * 2
        continue
    else:  
        r -= temp
        c -= temp
        answer += (temp ** 2) * 3
        continue

print(answer)