import sys
input = sys.stdin.readline

num = {
    " " : "0000000",
    "0" : "1111110",
    "1" : "0110000",
    "2" : "1101101",
    "3" : "1111001",
    "4" : "0110011",
    "5" : "1011011",
    "6" : "1011111",
    "7" : "1110010",
    "8" : "1111111",
    "9" : "1111011"
}

tk = int(input())
for _ in range(tk):
    answer = 0
    a, b = input().split()

    a = " " * (5 - len(a)) + a
    b = " " * (5 - len(b)) + b
    
    for i in range(5):
        for j in range(7):
            if num[a[i]][j] != num[b[i]][j]:
                answer += 1
    
    print(answer)