# n = int(input())
# arr = [list(map(int, input())) for _ in range(n)]

# def f(y, x, size):
#     temp = ""
#     char = str(arr[y][x])
#     if size == 1:
#         return str(arr[y][x])
#     else:
#         for i in range(y, y + size):
#             for j in range(x, x + size):
#                 if(str(arr[i][j]) != char):
#                     temp += "("
#                     temp += f(y, x, size//2)
#                     temp += f(y, x + size//2, size//2)
#                     temp += f(y + size//2, x, size//2)
#                     temp += f(y + size//2, x + size//2, size//2)
#                     temp += ")"
#                     return temp

#     return str(arr[y][x])

# res = f(0, 0, n)

# print(res)



import sys
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

def recursion(y, x, n):
    if n == 1:
        return graph[y][x]
    
    for i in range(y, y + n):
        for j in range(x, x + n):
            if graph[i][j] != graph[y][x]:
                ret = "("
                ret += recursion(y, x, n // 2)
                ret += recursion(y, x + (n // 2), n // 2)
                ret += recursion(y + (n // 2), x, n // 2)
                ret += recursion(y + (n // 2), x + (n // 2), n // 2)
                ret += ")"
                return ret

    return graph[y][x]

print(recursion(0, 0, n))