n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(int(input()))

answer = 0
for i in arr[::-1]:
    answer += k // i
    k = k % i

print(answer)