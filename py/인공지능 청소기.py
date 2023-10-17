import sys
input = sys.stdin.readline

for _ in range(int(input())):
	x, y, n = map(int, input().split())
	
	msg = "NO"
	if n >= abs(x) + abs(y):
		if n == abs(x) + abs(y):
			msg = "YES"
		elif (n - (abs(x) + abs(y))) % 2 == 0:
			msg = "YES"
		
	print(msg)