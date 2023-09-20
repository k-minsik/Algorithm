answer = 0
arr = [list(input()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if arr[i][j] == 'F':
                answer += 1
    
print(answer)