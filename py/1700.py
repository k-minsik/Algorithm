n, k = map(int, input().split())
arr = list(map(int, input().split()))

using = []
answer = 0
for i in range(k):
    if arr[i] in using:
        continue
    
    if len(using) < n:
        using.append(arr[i])
        continue

    last = 0
    temp = 0
    for j in using:
        if j not in arr[i:]:
            temp = j
            break
        elif arr[i:].index(j) > last:
            last = arr[i:].index(j)
            temp = j

    using[using.index(temp)] = arr[i]
    answer += 1

print(answer)