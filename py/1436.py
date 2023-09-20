n = int(input())

i = 0
num = 666
while True:
    if str(num).find('666') >= 0: i += 1
    if i == n:
        break
    num += 1

print(num)