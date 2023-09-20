import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def postOrder(s, e):
    if s > e:
        return
    
    m = e + 1
    for i in range(s + 1, e + 1):
        if data[i] > data[s]:
            m = i
            break

    postOrder(s + 1, m - 1)
    postOrder(m, e)
    print(data[s])

data = []
while True:
    try:
        data.append(int(input()))
    
    except:
        break

postOrder(0, len(data) - 1)