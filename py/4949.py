# arr = ['(', ')', '[', ']']

# while True:
#     s = input().rstrip()
#     if s == ".": break
#     s = list(s)

#     st = []
#     while s:
#         temp = s.pop()
#         if temp in arr:
#             if st:
#                 if (st[-1] == ")" and temp == "(") or (st[-1] == "]" and temp == "["):
#                     st.pop()
#                 else:
#                     if temp == "(" or temp == "[":
#                         st.append(temp)
#                         break
#                     else:
#                         st.append(temp)
#             else:
#                 if temp == "(" or temp == "[":
#                         st.append(temp)
#                         break
#                 else:
#                     st.append(temp)
    
#     if st: print("no")
#     else: print("yes")

import sys
input = sys.stdin.readline

def check(string):
    stack = []

    for i in string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '[':
            stack.append(i)
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    
    return True


while True:
    string = input().rstrip()
    if string == ".":
        break
    
    print("yes") if check(string) else print("no")