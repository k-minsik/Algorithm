import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0 
for i in arr:
    answer += 1
    i -= b
    if i > 0:
        if i % c == 0:
            answer += i // c
        else:
            answer += i // c + 1

print(answer)