from collections import deque
from math import gcd
import re
import ssl


def level2_1(n):
    ans = 0 
    while n != 0:
        if n % 2 == 0:
            n //= 2 
        else: 
            n -= 1
            ans += 1

    return ans

def level2_2(n):
    cnt = format(n, 'b').count('1')

    while True:
        n += 1
        cnt2 = format(n, 'b').count('1')
        if cnt == cnt2:
            return n


def solution(s):
    if len(s) % 2 == 1: return 0

    a = list(s[:-1])
    b = [s[-1]]

    for i in a[::-1]:

        if b and b[-1] == i:
            b.pop()
        else:
            b += i
    
    return 0 if b else 1


    

print(solution("baabaa"))
print(solution("cdcd"))




