
from bisect import bisect, bisect_left
from curses.ascii import isalpha
from inspect import BoundArguments
from itertools import combinations, permutations, product
from math import ceil, gcd, sqrt
import re
from xml.etree.ElementTree import C14NWriterTarget
from zoneinfo import available_timezones



def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    count = {subject : 0 for subject in id_list}

    for i in set(report):
        count[i.split()[1]] += 1

    for j in set(report):
        if count[j.split()[1]] >= k:
            answer[id_list.index(j.split()[0])] += 1

    return answer


def solution2(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    correct = 0
    cnt = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            correct += 1

    answer = [rank[correct + cnt], rank[correct]]

    return answer


def solution3(new_id):
    answer = ''
    
    id = new_id.lower()

    for i in id:
        if i.islower() or i.isdigit() or (i in ['-', '_', '.']):
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip(".")

    if len(answer) == 0:
        answer += 'a'

    if len(answer) >= 16:
        answer = answer[0:15]

    if answer[len(answer)-1] == '.':
        answer = answer[0:len(answer)-1]

    while len(answer) < 3:
        answer += answer[len(answer)-1]

    return answer


def solution4(s):
    answer = 0

    num_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}

    for i in num_dict:
        if i in s:
            s = s.replace(i, num_dict[i])
    
    answer = int(s)

    return answer


def sol5(numbers, hand):
    result = ''
    left_pos = '*'
    right_pos = '#'

    pad = {1:[1, 1], 2:[1, 2], 3:[1,3],
    4:[2, 1], 5:[2, 2], 6:[2,3],
    7:[3, 1], 8:[3, 2], 9:[3,3],
    '*':[4, 1], 0:[4, 2], '#':[4,3]}

    for i in numbers:
        if i in [1, 4, 7]:
            result += "L"
            left_pos = i
        elif i in [3, 6, 9]:
            result += "R"
            right_pos = i
        else:
            if hand == "left":
                if (abs(pad[left_pos][0] - pad[i][0]) + abs(pad[left_pos][1] - pad[i][1])) <= (abs(pad[right_pos][0] - pad[i][0]) + abs(pad[right_pos][1] - pad[i][1])):
                    result += "L"
                    left_pos = i
                else:
                    result += "R"
                    right_pos = i
            else:
                if (abs(pad[left_pos][0] - pad[i][0]) + abs(pad[left_pos][1] - pad[i][1])) >= (abs(pad[right_pos][0] - pad[i][0]) + abs(pad[right_pos][1] - pad[i][1])):
                    result += "R"
                    right_pos = i
                else:
                    result += "L"
                    left_pos = i

    return result


def sol6(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


def sol7(numbers):
    answer = 0

    for i in range(10):
        if i not in numbers:
            answer += i

    return answer


def sol8(a, b):
    # answer = 0
    # for i, j in zip(a, b): answer += i*j
    return sum([x*y for x, y in zip(a, b)])

def sol9(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        sol = ""
        comp = s[0:i]
        count = 1
        for j in range(i, len(s), i):
            if comp == s[j:j+i]:
                count += 1
            else:
                sol += str(count) + comp if count >= 2 else comp
                comp = s[j:j + i]
                count = 1
            
        sol += str(count) + comp if count >= 2 else comp
    
        answer = min(answer, len(sol))
    
    return answer


def sol10(record):
    answer = []
    user = {}
    
    for records in record:
        if records.startswith("Enter") or records.startswith("Change"):
            user[records.split()[1]] = records.split()[2]
        
    for records in record:
        if records.startswith("Enter"):
            comm = user[records.split()[1]] + "님이 들어왔습니다."
            answer.append(comm)
        elif records.startswith("Leave"):
            comm = user[records.split()[1]] + "님이 나갔습니다."
            answer.append(comm)
    return answer


def sol11(N, stages):
    answer = []
    fail = {}

    for i in range(1, N+1):
        suc = 0
        trying = stages.count(i)
        for j in stages:
            if j > i:
                suc += 1
        if suc + trying != 0:
            fail[i] = trying / (suc + trying)
        else:
            fail[i] = 0

    for key, value in sorted(fail.items(), key = lambda item: item[1], reverse = True):
        answer.append(key)
        
    return answer


def sol13(str1, str2):
    comp1, comp2 = [], []
    str1, str2 = str1.lower(), str2.lower()

    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            comp1.append(str1[i:i+2])
    
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            comp2.append(str2[i:i+2])
    
    ry = set(comp1) & set(comp2)
    gkq = set(comp1) | set(comp2)

    ry_ = sum([min(comp1.count(a), comp2.count(a)) for a in ry])
    gkq_ = sum([max(comp1.count(b), comp2.count(b)) for b in gkq])

    return int((ry_/gkq_)*65536) if gkq_ else 65536


def sol14(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        temp = str(bin(i|j)[2:].zfill(n))
        print(temp)
        temp = temp.replace('1', '#')
        temp = temp.replace('0', ' ')
        answer.append(temp)

    return answer


def sol15(dartResult):
    point = []
    dartResult = dartResult.replace('10', 'A')

    for i in dartResult:
        if i.isdigit() or i == 'A':
            point.append(10 if i == 'A' else int(i))
        elif i == 'D':
            point[-1] = point[-1] ** 2
        elif i == 'T':
            point[-1] = point[-1] ** 3
        elif i == '#':
            point[-1] = -point[-1]
        elif i == '*':
            if len(point) > 1:
                point[-1] = point[-1] * 2
                point[-2] = point[-2] * 2
            else:
                point[-1] = point[-1] * 2
                
    return sum(point)


def sol12(orders, course):    
    # orders, course = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
    # orders2, course2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]
    # orders3, course3 = ["XYZ", "XWY", "WXA"], [2,3,4]
    answer = []
    foods = []
    result = {}
    results = {}
    change = str.maketrans("(',)", "    ")

    for order in orders:
        for food in order:
            foods.append(food)

        for time in course:
            menu = list(combinations(sorted(foods), time))

            for setmenu in menu:
                setmenu = str(setmenu).translate(change).replace(" ", "")
                if setmenu not in result:
                    result[setmenu] = 1
                else:
                    result[setmenu] += 1
        menu = []
        foods = []

    for i in course:
        for key, value in result.items():
            if len(key) == i:
                results[key] = value
        for key2, value2 in results.items():
            if value2 == max(results.values()) and max(results.values()) > 1:
                answer.append(key2)
        results = {}
                
    return sorted(answer)



def sol16(fees, records):
    # fee2 = [120, 0, 60, 591]
    # info2 = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

    answer = []
    record = {}
    time_record = {}

    for info in records:
        time = int(info.split(" ")[0].split(":")[0])*60 + int(info.split(" ")[0].split(":")[1])

        if info.split(" ")[1] not in time_record:
            time_record[info.split(" ")[1]] = 0

        if info.split(" ")[2] == 'IN':
            record[info.split(" ")[1]] = time
        elif info.split(" ")[2] == 'OUT':
            time_record[info.split(" ")[1]] += time - record[info.split(" ")[1]]
            del(record[info.split(" ")[1]])

    if record:
        for num, time in record.items():
            time_record[num] += 1439 - time

    for num, times in sorted(time_record.items()):
        if times >= fees[0]:
            answer.append(fees[1] + ceil((times-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])

    return answer

def sol17(info, query):
    answer = []
    info_dict = {}

    for i in range(len(info)):
        infol = info[i].split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    info_dict[tmp] = [int(myval)]

    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in info_dict:  # query의 key가 info_dict의 key로 존재하면
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))

                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

def sol18(s):
    answer = []
    arr, arr2 = [], []
    temp = s[2:-2].split("},{")
    
    for i in temp:
        j = i.split(",")
        for k in j:
            arr2.append(int(k))
        arr.append(arr2)
        arr2 = []

    arr.sort(key=len)
    answer.append(arr[0][0])
    
    for i in range(len(arr)-1):
        answer.append(list(set.difference(set(arr[i+1]), set(arr[i])))[0])
            
    return answer

def sol19(cacheSize, cities):
    answer = 0
    city = []
    for i in cities:
        if cacheSize == 0:
            answer += 5
        elif i.lower() in city:
                answer += 1
                city.remove(i.lower())
                city.insert(0, i.lower())
        else:
            if len(city) == cacheSize:
                city.pop()
            city.insert(0, i.lower())
            answer += 5
    return answer


def solution20(placess):
    def sol20(places):
        point = []

        for i in range(len(places)):
            for j in range(len(places)):
                if places[i][j] == 'P':
                    point.append((i,j))

        for a in range(len(point)):
            for b in range(a+1, len(point)):
                if (abs(point[a][0]-point[b][0])+abs(point[a][1]-point[b][1])) == 1:
                    return 0
                elif (abs(point[a][0]-point[b][0])+abs(point[a][1]-point[b][1])) == 2:
                    if point[a][0] == point[b][0]: #같은 행
                        if places[point[a][0]][int((point[a][1]+point[b][1])/2)] != 'X':
                            return 0
                    elif point[a][1] == point[b][1]: #같은 열
                        if places[int((point[a][0]+point[b][0])/2)][point[a][1]] != 'X':
                            return 0
                    else: # 대각
                        if places[point[a][0]][point[b][1]] == 'O' or places[point[b][0]][point[a][1]] == 'O':
                            return 0

        return 1

    answer = []
    for i in placess:
        answer.append(sol20(i))
    
    return answer


def sol21(n, lost, reserve):
    count = 0
    lost = set(lost)
    reserve = set(reserve)
    reserve = reserve.difference(lost)
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        elif i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            count += 1

    return n - count


def solution22(num):
    answer = []

    for i in range(len(num)-1):
        for j in range(i, len(num)-1):
            print(num[i], num[j+1])
            if num[i]+num[j+1] not in answer: answer.append(num[i]+num[j+1])

    return sorted(list(set(answer)))

def solution23(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
        elif answer[-1] != i:
            answer.append(i)

    return answer


def solution24(a, b):
    if a > b: a, b = b, a
    return sum(range(a, b+1))

def solution25(s):
    return True if s.lower().count('p') == s.lower().count('y') else False


def dirtn(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt

def solution26(a, b):
    answer = 0
    for i in range(a, b+1):
        if dirtn(i) % 2 == 1:
            answer += i    
    return sum(range(a, b+1)) - answer*2

def solution27(n):
    dec = ''
    while n:
        n, t = n//3, n%3
        dec += str(t)

    return int(dec, 3)


def solution28(d, budget):
    cnt = 0
    d.sort()
    if sum([i for i in d]) <= budget:
        return len(d)

    for i in d:
        budget -= i 
        if budget < 0:
            break
        cnt += 1

    return cnt

def solution29(a, b):
    m = {1: 0, 2:31, 3:60, 4:91, 5:121, 6:152, 7:182, 8:213, 9:244, 10:274, 11:305, 12:335}
    d = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    return d[(m[a] + b -1) % 7]


def solution30(sizes):
    max_w, max_h = 0, 0
    for i in sizes:
        if i[0] < i[1]: i[0], i[1] = i[1], i[0]
        if i[0] > max_w: max_w = i[0]
        if i[1] > max_h: max_h = i[1]

    return int(max_h*max_w)

def solution31(n):
    return min([x for x in range(2, n) if n%x==1])


def solution32(price, money, count):
    for i in range(1, count+1):
        money -= price*i
    return abs(money)

def solution33(s):
    return s[len(s)//2] if len(s)%2==1 else s[len(s)//2-1:len(s)//2+1]

def solution34(arr, divisor):
    return [x for x in sorted(arr) if x%divisor==0] or [-1]

def solution35(strings, n):
    # dict = {i:j[n] for i,j in zip(sorted(strings), sorted(strings))}
    return [x for x, y in sorted({i:j[n] for i,j in zip(sorted(strings), sorted(strings))}.items(), key = lambda item:item[1])]

def solution36(arr1, arr2):
    row, col = len(arr1), len(arr1[0])
    for i in range(row):
        for j in range(col):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    return arr1

def solution37(n):
    result = []
    num = [1, 2, 4]

    while n:
        n, m = n // 3, n % 3
        result.insert(0, m)
    
    while True:
        if 0 in result[1:]:
            for i in range(1, len(result)):
                if result[i] == 0:
                    result[i-1] -= 1
                    if result[i-1] == 3: result[i-1] = 2
                    result[i] = 4
        else:
            break
    
    return str(int(''.join([str(i) for i in result])))
    
def solution38(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        print(queue)
        temp, idx = queue.pop(0)
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


def solution39(prog, speeds):
    answer, result = [], []
    for i, j in zip(range(len(prog)), speeds):
        if (100 - prog[i]) / j == int((100 - prog[i]) / j):
            answer.append((100 - prog[i]) // j)
        else:
            answer.append(int((100 - prog[i]) / j) + 1)
    
    idx = 0
    while idx < len(answer): # 4
        cnt = 1
        idx_ = idx
        if idx < len(answer) - 1: # 3
            for i in answer[idx_+1:]:
                if answer[idx_] >= i:
                    idx += 1
                    cnt += 1
                else: 
                    break 
        result.append(cnt)
        idx += 1
    return result
    
def cal(a, b, op):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b


def solution40(exp):
    answer = [-1]
    oper = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '-'], ['+', '-', '*'], ['-', '+', '*'], ['-', '*', '+']]
    mid = []

    str = ''
    for i in exp:
        if i.isdigit():
            str += i
            if i == exp[-1]:
                mid.append(int(str))
                str = ''
        else:
            mid.append(int(str))
            str = ''
            mid.append(i)

    for i in oper:
        mid2 = mid
        while len(mid2) > 1:
            for j in mid2:
                pass


    return max(answer)

def sol41(n):
    c1 = {500:1, 300:3, 200:6, 50:10, 30:15, 10:21}
    c2 = {512:1, 256:3, 128:7, 64:15, 32:31}
    n = int(input())
    for i in range(n):
        if a <= 21:
            for k, v in c1.items():
                if int(a) <= v: a = k
        else: a = 0
        if b <= 31:
            for k, v in c2.items():
                if int(b) <= v: b = k
        else: b = 0

    return (a+b)*100000


def sol42(n, k):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(i)
        if len(arr) == k:
            return arr[k-1]
    return 0
        
def sol43(n):
    str_ = ''
    arr = [i for i in bin(n)[:1:-1]]
    for i in range(len(arr)):
        if arr[i] == '1':
            str_ += (str(i) + ' ')
    return str_

def sol44(n):
    arr = [int(i) for i in n.split()]
    return min(arr), max(arr)

def sol45(n):
    answer = []
    for i in range(1, 11):
        a, b = input().split()
        n -= (int(a) - int(b))
        answer.append(n)
    return max(answer)

def sol46(n):
    arr =[0, 1, 1]
    for i in range(1, n-1):
        arr.append(arr[i] + arr[i+1])
    return arr[n]

def sol47(arr):
    h = sum(arr) - 100
    for i in list(combinations(arr, 2)):
        if i[0] + i[1] == h:
            arr.remove(i[0])
            arr.remove(i[1])
            break
    
    for i in sorted(arr):
        print(i)


def gcd(m,n):
    while n != 0:
       t = m%n
       m,n = n,t
    return abs(m)

def sol48(arr):
    print(sorted(arr[-3]))

def sol49():
    t = int(input())
    for i in range(t):
        arr = []
        n = input()
        for i in n.split():
            arr.append(int(i))
        print(sorted(arr)[-3])

def sol50(a, b):
    arr = [0]
    for i in range(1, int(b//2)):
        arr += [i] * i
    return sum(arr[a:b+1])

def sol51():
    a = int(input())
    b = int(input())
    arr = [False, False, True, True] + [True] * (b-3)
    for i in range(4, len(arr)):
        if arr[i] == True:
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    arr[i] = False
                    break

    prime = []
    for i in range(a, b+1):
        if arr[i] == True:
            prime.append(i)

    print(prime)
    if prime:
        print(sum(prime))
        print(min(prime))
    else:
        print(-1)


def sol52():
    a= input()
    b = [int(i) for i in input().split()]

    arr = [False, False, True, True] + [True] * (max(b)-3)
    for i in range(4, len(arr)):
        if arr[i] == True:
            for j in range(2, int(sqrt(i))+1):
                if i % j == 0:
                    arr[i] = False
                    break

    cnt = 0
    for i in b:
        if arr[i] == True:
            cnt += 1

    print(cnt)


def sol53():
    a = int(input())
    b = int((a*2)**0.5)
    arr = []
    for i in range(1, b*2):
        arr.append(int((i*(i+1)/2)))

    if a == 1: print(1)
    for i in arr:
        if a < i:
            print(arr.index(i))
            break   

    return 0


def sol54(sql):
    opcode = {'ADD':'00000', 'SUB':'00010', 'MOV':'00100', 'AND':'00110', 'OR':'01000', 'NOT':'01010', 'MULT':'01100', 'LSFTL':'01110', 'LSFTR':'10000', 'ASFTR':'10010', 'RL':'10100', 'RR':'10110',}
    opcodec = { 'ADDC':'00001', 'SUBC':'00010', 'MOVC':'00101', 'ANDC':'00111', 'ORC':'01001', 'MULTC':'01101', 'LSFTLC':'01111', 'LSFTRC':'10001', 'ASFTRC':'10011', 'RLC':'10101', 'RRC':'10111'}

    s = ''

    if sql[0] in opcode:
        s += opcode[sql[0]]
    elif sql[0] in opcodec:
        s += opcodec[sql[0]]
    
    s += '0'
    s += format(int(sql[1]), 'b').zfill(3)
    s += format(int(sql[2]), 'b').zfill(3)

    if sql[0] in opcode:
        s += format(int(sql[3]), 'b').zfill(3)
        s += '0'
    elif sql[0] in opcodec:
        s += format(int(sql[3]), 'b').zfill(4)

    print(s)

def sol55(s):
    i = 0
    l = list(s)
    while l:
        if i == len(l)-2:
            i = 0
        elif l[i] == l[i+1]:
            del l[i]
            del l[i+1]
            i += 1

    return 0 if s else 1


def sol56(h, w):
    world = [[0 for j in range(w)] for i in range(h)]
    # wall = list(map(int, input().split()))
    wall = [3, 1, 2, 3, 4, 1, 1, 2]
    water = 0
    l_h = wall[0]
    r_h = wall[-1]

    if wall[0] >= wall[-1]:
        for i in wall[-2:0:-1]:
            if i >= r_h:
                r_h = i
            else:
                water += (r_h - i)
                print(1, water)
    else:
        for i in wall[1:-1]:
            if i >= l_h:
                l_h = i
            else:
                water += (l_h - i)
                print(2, water)

    return water

def sol50(a, b):
    arr = [0]
    for i in range(1, 46):
        arr += [i] * i
    return sum(arr[a:b+1])


def sol51(len, w, t):
    ans = 0
    on, pos = [], []
    while t:
        if (sum(on) + t[0]) <= w:
            on.append(t.pop(0))
            pos.append(0)
            print(t, on, pos)
        for i in range(len(on)):
            pos[i] += 1
        if pos[0] == len:
            on.pop(0)
            pos.pop(0)
        ans += 1

    while on:
        pos[0] += 1
        if pos[0] == len:
            on.pop(0)
            pos.pop(0)
        ans += 1


    return ans+(len-1)

# print(solution(5))
# print(solution(6))
# print(solution(5000))

def solution(input_string):
    answer = ''
    input_string = input_string
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            c = input_string.count(input_string[i])
            if c > 1:
                if input_string.rfind(input_string[i]) - i > c-1:
                    answer += input_string[i]
            input_string = input_string.replace(input_string[i], ' ')
        
    
    return "".join(sorted(answer)) if answer else 'N'

# print(solution("edeaaabbccd"))
# print(solution("eeddee"))
# print(solution("string"))
# print(solution("zbzbz"))


from itertools import permutations

def solution(ability):
    max = 0
    sum = 0
    item = [i for i in range(len(ability))]

    for i in permutations(item, len(ability[0])):
        for j in range(len(i)):
                sum += ability[i[j]][j]
        if max < sum:
            max = sum
        sum = 0

    return max
    

# print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]	))
# print(solution([[20, 30], [30, 20], [20, 30]]))


def solution(queries):
    def check(lv, sq):
        w = ['RR', 'Rr', 'Rr', 'rr']
        if lv == 2:
            return w[sq]
        
        pa = check(lv-1, sq//4)
        if pa == 'Rr': 
            return w[sq%4]
        else:
            return pa


    answer = []

    for i in queries:
        lv, sq = i
        answer.append(check(lv, sq-1))

    return answer

# print(solution([[3, 5]]))
# print(solution([[3, 8], [2, 2]]))
# print(solution([[3, 1], [2, 3], [3,9]]))
# print(solution([[4, 26]]))



def solution(N, road, K):
    INF = int(1e5)
    graph = [[INF]*N for _ in range(N)]
    distance = [INF] * N

    for i in range(N):
        graph[i][i] = 0
    
    for i in road:
        graph[i[0]-1][i[1]-1] = min(graph[i[0]-1][i[1]-1], i[2])
        graph[i[1]-1][i[0]-1] = min(graph[i[1]-1][i[0]-1], i[2])

    idx = 0
    for i in range(N):
        distance[i] = graph[0][i]

    while idx < N:
        for i in range(N):
                if distance[i] > distance[idx] + graph[idx][i]:
                    distance[i] = distance[idx] + graph[idx][i]
        idx += 1

    cnt = 0
    for i in distance:
        if i <= K:
            cnt += 1
    print(graph)
    print(distance)
    return cnt


# print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
# print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))


def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        s = ''
        for j in i:
            if j in skill:
                s += j

        if skill.startswith(s):
            answer += 1

    return answer

# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
from collections import deque
def solution(dirs):
    answer = 0
    dir = {'U' : [1, 0], 'D' : [-1, 0], 'R' : [0, 1], 'L' : [0, -1]}
    now = deque()
    now.append((5, 5))
    history = []

    for i in dirs:
        x, y = now.popleft()
        nx = x + dir[i][0]
        ny = y + dir[i][1]
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            if [(x, y), (nx, ny)] not in history and [(nx, ny), (x, y)] not in history:
                history.append([(x, y), (nx, ny)])
                history.append([(nx, ny), (x, y)])
                answer += 1
            now.append((nx, ny))
        else:
            now.append((x, y))

    return answer

# print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))


def solution(A, B):
    answer = 0
    A = sorted(A, reverse=True)
    B = sorted(B)

    for i in A:
        if B[-1] > i:
            answer +=1
            B.pop()
        else:
            continue
    return answer

# print(solution([5,1,3,7], [2,2,6,8]))
# print(solution([2,2,2,2], [1,1,1,1]))
from math import ceil
def solution(n, stations, w):
    answer = 0
    now = 1

    for s in stations:
        answer += ceil(((s - w) - now) / (2 * w + 1))
        now = s + w + 1

    if now <= n:
        answer += ceil((n - now + 1) / (2 * w + 1))

    return answer

# print(solution(11, [4, 11] ,1))
# print(solution(16, [9], 2))

def solution(sticker):
    if len(sticker) < 4:
        return max(sticker)

    res1 = [0] * len(sticker) 
    res2 = [0] * len(sticker)

    res1[0] = sticker[0]
    res1[1] = sticker[0]
    res2[0] = 0
    res2[1] = sticker[1]

    for i in range(2, len(sticker)):
        if i == len(sticker) - 1:
            res2[i] = max(res2[i-1], res2[i-2] + sticker[i])

        else:
            res1[i] = max(res1[i-1], res1[i-2] + sticker[i])
            res2[i] = max(res2[i-1], res2[i-2] + sticker[i])

    return max(res1[-2], res2[-1])

print(solution([14,6,5,11,3,9,2,10]))
print(solution([1,3,2,5,4]))
