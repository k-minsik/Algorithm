l = int(input())
s = list(input().rstrip())
answer = 0

for i in range(l):
    answer += (ord(s[i]) - 96) * (31 ** i)


print(answer % 1234567891)