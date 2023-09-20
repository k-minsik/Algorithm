arr = []
for i in range(5):
    s = list(input().rstrip())
    while len(s) < 15:
        s.append(-1)
    arr.append(s)

for i in range(15):
    for j in range(5):
        if arr[j][i] != -1:
            print(arr[j][i], end="")
