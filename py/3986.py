# res = 0

# n = int(input())
# for _ in range(n):
#     stack = []
#     s = list(input().rstrip())
#     stack.append(s.pop())

#     while s:
#         temp = s.pop()
#         if stack:
#             if stack[-1] == temp:
#                 stack.pop()
#             else:
#                 stack.append(temp)
#         else:
#             stack.append(temp)
        
        
#     if not stack: res += 1

# print(res)



import sys
input = sys.stdin.readline

answer = 0 
n = int(input())
for _ in range(n):
    word = list(input().rstrip())
    stack = [word.pop()]

    while word:
        if stack:
            if stack[-1] == word[-1]:
                stack.pop()
                word.pop()
            else:
                stack.append(word.pop())
        else:
            stack.append(word.pop())

    if not stack:
        answer += 1

print(answer)
