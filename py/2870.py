n = int(input())

answer = []
for _ in range(n):
    s = input().rstrip();

    temp = ""
    for i in range(len(s)):
        if s[i].isalpha():
            if temp:
                answer.append(int(temp))
                temp = ""
        else:
            temp += s[i]
    
    if temp:
        answer.append(int(temp))

answer.sort()

for i in answer:
    print(i)
