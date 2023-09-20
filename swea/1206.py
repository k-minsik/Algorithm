for tk in range(1, 11):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split()))

    # for i in range(2, n-2):
    #     if arr[i] <= max(max(arr[i-2:i]), max(arr[i+1:i+3])):
    #         continue
    #     else:
    #         answer += arr[i] - max(max(arr[i-2:i]), max(arr[i+1:i+3])) 
    
    i = 2
    while i < n:
        if arr[i] <= max(max(arr[i-2:i]), max(arr[i+1:i+3])):
            i += 1
        else:
            answer += arr[i] - max(max(arr[i-2:i]), max(arr[i+1:i+3])) 
            i += 2



    print('#{} {}'.format(tk, answer))