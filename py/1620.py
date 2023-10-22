# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# mon = [0]
# mon2 = {}

# for i in range(1, n+1):
#     temp = input().rstrip()
#     mon.append(temp)
#     mon2[temp] = i

# for _ in range(m):
#     quiz = input().rstrip()
#     if quiz[0].isalpha():
#         print(mon2[quiz])
#     else:
#         print(mon[int(quiz)])


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemonDict = {}
pokemonArray = ['']

for i in range(1, n + 1):
    name = input().rstrip()
    pokemonDict[name] = i
    pokemonArray.append(name)

for _ in range(m):
    quiz = input().rstrip()
    if quiz.isdigit():
        print(pokemonArray[int(quiz)])
    else:
        print(pokemonDict(quiz))