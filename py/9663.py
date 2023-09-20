n = int(input())
arr = [0 for _ in range(n)]
answer = 0

def possible(cur):
    for i in range(cur):
        if arr[i] == arr[cur] or abs(i - cur) == abs(arr[i] - arr[cur]):
            return False
    
    return True
        
def nqueen(cur):
    global answer
    if cur == n:
        answer += 1
        return

    for i in range(n):
        arr[cur] = i

        if possible(cur):
            nqueen(cur+1)
nqueen(0)
print(answer)