# import sys
# input = sys.stdin.readline

# def func(s, e, level):
#     mid = (s + e) // 2

#     if level == k or s == e:
#         temp[level-1].append(arr[mid])
#         return

#     temp[level-1].append(arr[mid])
#     func(s, mid - 1, level + 1)
#     func(mid+1, e, level + 1)


# k = int(input())
# arr = list(map(int, input().split()))
# temp = [[] for _ in range(k)]
# l = 2 ** k - 1

# func(0, l, 1)

# for i in temp:
#     for j in i:
#         print(j, end = " ")
#     print()


import sys
input = sys.stdin.readline

k = int(input())
nums = list(map(int, input().split()))
graph = [[] for _ in range(k)]

def reverseInOrder(r, l, lv):
    mid = (r + l) // 2

    if lv == k - 1:
        graph[lv].append(nums[mid])
        print(lv, nums[mid])
        return
        
    graph[lv].append(nums[mid])
    reverseInOrder(r, mid - 1, lv + 1)
    reverseInOrder(mid + 1, l, lv + 1)

reverseInOrder(0, len(nums), 0)
for i in graph:
    print(*i)