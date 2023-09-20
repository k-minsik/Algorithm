goal = int(input())
cur = 100
answer = abs(cur - goal)

k = int(input())
if k == 0:
    print(min(answer, len(str(goal))))
elif k == 10:
    print(answer)
else:
    cant = list(map(int, input().split()))

    for i in range(1000001):
        flag = 0
        for j in str(i):
            if int(j) in cant:
                flag = 1
                break
        
        if flag:
            continue
        
        answer = min(answer, len(str(i)) + abs(i - goal))

    print(answer)