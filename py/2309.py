from itertools import combinations
arr = []
res = 0

for i in range(9):
    temp = int(input())
    res += temp
    arr.append(temp)

for i in list(combinations(arr, 2)):
    if res - i[0] - i[1] == 100:
        arr.remove(i[0])
        arr.remove(i[1])
        break
    
arr = sorted(arr, reverse=False)
# for i in arr:
print(i)