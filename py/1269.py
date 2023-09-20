import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
temp = len(arr & arr2)

print(arr & arr2)
print(len(arr) + len(arr2) - temp * 2)