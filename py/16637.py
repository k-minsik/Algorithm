import sys
input = sys.stdin.readline

n = int(input())
exp = str(input().rstrip())
nums = []
opers = []
answer = -1e10

for i in range(n):
    if i % 2 == 0:
        nums.append(int(exp[i]))
    else:
        opers.append(exp[i])

def operator(a, o, b):
    if o == '+':
        return  a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    
def recursion(idx, num):
    global answer

    if idx == len(nums) - 1:
        answer = max(answer, num)
        print("answer = " + str(answer))
        return
    

    recursion(idx + 1, operator(num, opers[idx], nums[idx + 1]))

    if idx + 2 <= len(nums) - 1:
        recursion(idx + 2, operator(num, opers[idx], operator(nums[idx+1], opers[idx+1], nums[idx+2])))
    

recursion(0, nums[0])
print(answer)